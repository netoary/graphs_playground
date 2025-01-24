import numpy as np
import gymnasium as gym
from random import randint
from sage.all import *
from gnn.utils import possibleMoves, takeHangingEdges, move, unmove, takeHangingEdges_v2, separa_cores_por_vertice, define_estado_atual, canonicalDecomposition, extractColor
from gnn.action import ActionBox, ActionDiscrete, ActionMultiDiscrete
from gymnasium.spaces import Graph as GraphGym, Box, Discrete, GraphInstance, Dict, MultiDiscrete
from typing import List, Optional
from collections import deque
from torch_geometric.data import Data, Batch
import torch
from gnn.gnn import GCNWithEdgeFeatures

old_observation_len = 30
# max_perfect_matchings = 20 # alguns planares
# max_perfect_matchings = 100 # planares
# max_perfect_matchings = 14 # K6
max_perfect_matchings = 25 # 8, 10 e 12 vértices

class GraphDecompositionEnv(gym.Env):
    def __init__(self, k = 5, G = None):
        super().__init__()
        # self.graph_list = [
        #     "O|fIJC`CGo``?`?w_EW?|",
        #     # "QtfIID`GH_b@A@@__WGB`?F_?Bw",
        #     # "S|fIBC`CGo`_@`?__[G@`?EC?KG?MG?A{", "StfIAD`GH_B@B@@__OGE@?[C?Ow?pG?]C", "S|fIIC_KGo`o?p?O_KG@@?MC?GW?MG?Bk", "StfIID`GH_b@A@@__WGA@?KC?[G?Cw?Fc", "StfIID`G@_b@B`?o?KG@`?CC?[G?EW?Bs", "StfIID`G@_b@B@?__WGB@?KC?PG?{G?Bw",
        #     # "U|bIBCpCGo`@B?@__OGE@?KC?[G?GW?KC?B`??Kw", "U|fIJ?pCGO`@@`?__OGA@?[C?WW?W??MC?@b??Lg", "U|fIAC`GG_b@B@@__OGE@?WC?oG?oG?[C?@b??NG", "UtfIID`GH_b?A@@__WGB`?E??KG?KG?EC??x??Bw", "UtfAID`G@_b@A@B?_oGE@?WC?oG?_G?{C?Ba??Fg", "UtfIID`GH_b?B@?__WGA@?KC?WG?WG?MC?@p??Fg", "U|fIBCpEGO_`@@?__OGF`?AG?KG?KG?EC?@h??Bw", "U|fII?`KGo``?`?__WGA@?WC?{??CW?EC?@p??Ew", "U|fIB?pEGW_o?`?__WGBo?B??EG?EG?BC??x??Bw", "U|fII?`KGo``?`?__WGA@?WC?wG?KG?EC?@p??Ew", "UtfIID_GH_b@B@?__WGA@?WC?oG?oG?MC?@p??Fg", "U|fIB?pEGW_o?`?__WGB@?EC?KG?KG?EC?@p??Bw", "U|fII?`KGo``?`?__WGA@?WC?oG?[G?EC?@p??FW", "U|eII@`KGo``@_?__WGA@?]??CW?KG?EC?@p??Dw", 
        #     # "W|fIIC`KGo@@@`?o_KG@`?CC?GG?WG?KC?@@??MG??X_??|", "W|eIID_KGo@`@`?o_GGB@?KC?WG?OG?KC?@`??KG??[_??^", "WtbIID`GH_a@E@A?`o?E@?WC?OG?wG?M??@@??[G??X_??|", "WtfIID`GH_b?B@?__WGA@?KC?WG?W??MC?@B??KG??w_??v", "WtfIID`GH_b@B@?__WGA@?KC?OG?OG?MC?@B??KG??w_??v", "WtfIID`GH_b?B@?_?WGB@?CC?WG?WG?KC?B@??QG?Bo_??}", "WtfIAD`GH_b@B?@__OGE@?WC?OG?wG?GK?A@??wG?@`_?@l", "WtfIID_GH_a@A@B__WWA@?WC?_G?_G?wC?CB??cG??w_??v", "WtfIID_GH_b?B`?p_GGB@?GC?OG?oG?WC??`??MG??X_??|", "W|eII@`KGo@`@`?__WGA@?OC?oG?oG?[C?@@??[G??p_?@t", "WtfIID`GH?a@E?B?_OGE??[C?WW?WG?GC?E@??wG?@B_?EX", 
        #     # "YtfIID`G@_b?B@?__WGB@?KC?OG?oG?WC?F???OG?@o_??b??@p???\_", "YtfIID`GH_B@B??__OGA@?[C?OW?o??WC?E@??oG?B?_?E`??@b???{_", "YtfIID`GH_b@B??__OGA@?WC?OG?w??KC?B@??WG?@__?B`??@F??@w_", "YtfIID`G@_b@B??__OGA@?WC?oG?_??wC?EB??og?B?_?E@??F@??@b_", "Y|eIID_KGo@`@_?o_GGA@?GC?oG?oG?WC?E@??wG?@__?B@??B`???Z_", "YtfIAD`GH_b@B?@__OGE@?[??OG?WG?KC?A@??WG?@__?B`??@w???N_", "Y|fIAC`K?o`_@`?__W?B@?GC?oG?oG?WC?F@??OG?B?_?F@??AF??@s_", "YtfIID`GH?a@E@B_?OGA@?WC?OG?oG?WC?E@??wG?@_??B`??@b???]_", "Y{fIJC`KG_b?B@?_?[G@o?AC?GG?GG?KC?B@??OG?Bo??@b??@d???{_", "YtfIAD`G@_b@B?@__OGE??WC?oG?_??wC?EB??wG?@C_?E@??F@??@b_", "YtfII@`GH_B@B_?_?WGA@?[C?OW?oG?WC?E@??oG?A?_?M@??@b???]_", 
        # ]
        # self.graph_list = ['E~~w']
        self.graph_list = [
            "ImetJomQw",
            "ScMU?CC@@??\IAt@HCQDOKCC`Q?Ro?A`W",
            "]Ao_OgGH@??@@@@AA@AA?OGKB_??eC?_C?DEG_G?B????PDGGDACDGOP@?Gc_K??O_?EEA@OO?",
            "g@??A?cO?_?G?G?A??[CG??CW??CGSO_@_G???SEa?G?WO_?gA?G?AC?@_AA?E@?_G??GO??_OW?C??C??CK?C@BG?CGS?O???GC@i@???@CG?OAG??_J?P@?_?@?GF???O",
            "q?_??GG_@???AGC@?AO?AC?CC?y_????@??????GCG??@CA?@C?`???A??O__?A???`?C?O?W??`??_?G?wGG??`?GcA?G@?W?C@@C?A??P?C?O?OO?O???G??G?C??COC??o???_D???AK?d?C?????K????DO?_@a?@??_A??@O?@AA@???_@GCA?C?G??_?H?_?Q?OA??_?",
        ]
        G = G or Graph(self.graph_list[0])
        self.nodes_number = int(G.order())
        self.edge_number = int(self.nodes_number * k / 2)
        self.element_number = int(self.edge_number / 5)
        self.dims = [self.nodes_number, self.nodes_number, self.element_number, self.nodes_number, self.nodes_number, self.element_number]
        self.observation_space = self._observation_space()
        self.action_space = self._actions_space()
        self.possible_actions = np.arange(sum(self.dims))
        self.possible_moves = []
        self.cont_invalid = 0
        self.step_counter = 0
        self._reset_prev_observation()
        self.mapping_action = {
            0 : '0100', 
            1 : '0110', 
            2 : '0102', 
            3 : '0112', 
            4 : '0122', 
            5 : '0200', 
            6 : '0210', 
            7 : '0220', 
            8 : '0301', 
            9 : '0302', 
            10 : '0312', 
            11 : '0322', 
            12 : '1100', 
            13 : '1101', 
            14 : '1112', 
            15 : '1200', 
            16 : '1201', 
            17 : '1202', 
            18 : '1203', 
            19 : '1211', 
            20 : '1222', 
            21 : '1223', 
            22 : '1301', 
            23 : '1302', 
            24 : '1312', 
            25 : '2200', 
            26 : '2201', 
            27 : '2202', 
            28 : '2203', 
            29 : '2212', 
            30 : '2301', 
            31 : '2302', 
            32 : '2312', 
            33 : '2322', 
            34 : '2332', 
            35 : '3312', 
            36 : '3322',
        }
        # self.mapping_action = ['0100', '0102', '0112', '0122', '0200', '0210', '0301', '0302', '0312', '0322', '1100', '1101', '1112', '1200', '1201', '1202', '1203', '1211', '1222', '1223', '1301', '1302', '1312', '2200', '2201', '2202', '2203', '2212', '2301', '2302', '2312', '2322', '3312', '3322'] # alguns planares
        # self.mapping_action = ['0221', '1021', '1100', '1112', '1211', '1301', '1302', '1321', '1333', '2102', '2110', '2111', '2113', '2122', '2221', '2200', '2231', '2333', '2301', '3133', '3122', '3110', '3120', '3313', '3322', '3312', '3323'] # K6
        self.mapping_action = ["0100", "0102", "0112", "0122", "0200", "0201", "0211", "0221", "0301", "0302", "0311", "0312", "0313", "0321", "0322", "0323", "1100", "1101", "1102", "1103", "1112", "1123", "1200", "1201", "1202", "1203", "1211", "1231", "1222", "1223", "1301", "1302", "1303", "1312", "1322", "3131", "1332", "1333", "2200", "2201", "2202", "2203", "2212", "2213", "2301", "2302", "2303", "2311", "2312", "2331", "2322", "2323", "2333", "3312", "3313", "3322", "3323"] # 8, 10 e 12 vértices
        self.mapping_action_repeat = ['0100', '0110', '0102', '0112', '0122', '0200', '0210', '0220', '0301', '0302', '0312', '0322', '1100', '1101', '1112', '1200', '1201', '1202', '1203', '1211', '1222', '1223', '1301', '1302', '1312', '2200', '2201', '2202', '2203', '2212', '2301', '2302', '2312', '2322', '2332', '3312', '3322']
        self.gnn_model = GCNWithEdgeFeatures()  # Definindo a GNN com features de aresta

    def action_masks(self) -> List[bool]:
        self.valid_actions = []
        for possible_move in self.possible_moves:
            self._move(possible_move)
            edges = extractColor(self.current_graph, possible_move[0][2])
            t1 = self._definir_tipo_trilha(Graph(edges))
            edges = extractColor(self.current_graph, possible_move[1][2])
            t2 = self._definir_tipo_trilha(Graph(edges))

            if self.tipo_trilha[possible_move[0][2]] + self.tipo_trilha[possible_move[1][2]] + t1 + t2 in self.mapping_action:
                self.valid_actions.append(self.tipo_trilha[possible_move[0][2]] + self.tipo_trilha[possible_move[1][2]] + t1 + t2)
            elif self.tipo_trilha[possible_move[1][2]] + self.tipo_trilha[possible_move[0][2]] + t1 + t2 in self.mapping_action:
                self.valid_actions.append(self.tipo_trilha[possible_move[1][2]] + self.tipo_trilha[possible_move[0][2]] + t1 + t2)
            elif self.tipo_trilha[possible_move[0][2]] + self.tipo_trilha[possible_move[1][2]] + t2 + t1 in self.mapping_action:
                self.valid_actions.append(self.tipo_trilha[possible_move[0][2]] + self.tipo_trilha[possible_move[1][2]] + t2 + t1)
            elif self.tipo_trilha[possible_move[1][2]] + self.tipo_trilha[possible_move[0][2]] + t2 + t1 in self.mapping_action:
                self.valid_actions.append(self.tipo_trilha[possible_move[1][2]] + self.tipo_trilha[possible_move[0][2]] + t2 + t1)

            self._unmove(possible_move)
        aux = [action in self.valid_actions for action in self.mapping_action]
        return aux

    def _reset_prev_observation(self):
        self.prev_observation = deque(maxlen=old_observation_len)
        for _ in range(old_observation_len):
            self.prev_observation.append(np.array([-1] * 9))


    def _get_gnn_embeddings(self):
        """
        Atualizado para incluir features mais ricas, como cor das arestas e proximidade de troca de cores
        """
        edges_list = self.current_graph.edges()
        color_map = {}
        vertex_map = {}
        for edge in edges_list:
            _ = color_map.setdefault(edge[2], [])
            color_map[edge[2]].append(edge)
            _ = vertex_map.setdefault(edge[0], [])
            vertex_map[edge[0]].append(edge[2])
            _ = vertex_map.setdefault(edge[1], [])
            vertex_map[edge[1]].append(edge[2])
        
        self.tipo_trilha = {}
        for color, edges in color_map.items():
            self.tipo_trilha[color] = self._definir_tipo_trilha(Graph(edges))

        edge_index = torch.tensor(list(self.current_graph.edges(labels=False)), dtype=torch.long).t().contiguous()

        # Features dos vértices: grau do vértice e a proximidade de arestas de cores diferentes
        vertex_features = []
        vertices = self.current_graph.vertices()
        for vertex in vertices:
            edges_of_this_vertex = self.current_graph.edges(vertex)
            number_of_diff_colors = len(set([i[2] for i in edges_of_this_vertex]))
            # Proximidade de troca de cores (quantas arestas vizinhas têm cores diferentes)
            color_diff_neighbors = 0
            for i in edges_of_this_vertex:
                for j in edges_of_this_vertex:
                    if i != j:
                        if i[2] != j[2]:
                            color_diff_neighbors += 1
            vertex_features.append([number_of_diff_colors, color_diff_neighbors/2])
        
        vertex_features = torch.tensor(vertex_features, dtype=torch.float)

        # Features das arestas: cor atual e progresso da decomposição
        edge_features = []
        edges = self.current_graph.edges()
        for edge in edges:
            ex = extractColor(self.current_graph, edge[2])
            edge_type = self._definir_tipo_trilha_int(Graph(ex))
            minimum_number_of_moves = {
                0: 0,
                1: 1,
                2: 1,
                3: 2,
            }
            # Progresso: número de arestas restantes no caminho atual
            progress = minimum_number_of_moves.get(edge_type, 0)
            edge_features.append([edge_type, progress])

        edge_features = torch.tensor(edge_features, dtype=torch.float)

        # Dados do PyTorch Geometric
        data = Data(x=vertex_features, edge_index=edge_index, edge_attr=edge_features)
        data.batch = torch.zeros(40, dtype=torch.long)  # Simula um único grafo (batch size de 1)

        # Aplicar a GNN com pooling global
        graph_embedding = self.gnn_model(data)
        return graph_embedding.detach().numpy()

    def _get_obs(self):
        """
        Temos dois dicionários, um de cores, onde cada chave é uma cor e o valor é uma lista com as arestas daquela cor.
        Um de vértices, tendo vértices como chaves e uma lista de cor que o vértice está colorido.

        Para toda aresta:
            preenchemos os dicionários de cores e vértices.

        Para cada cor, verificamos qual tipo de trilha ela representa.

        Geramos uma lista (grafo auxiliar) todo preenchido com zero.

        para cada véritice: 
            identificamos os tipos de trilhas que passam por ele (e tem grau maior que 1)
            incrementamos o valor na posição correspondente
        """
        edges_list = self.current_graph.edges()
        color_map = {}
        vertex_map = {}
        for edge in edges_list:
            _ = color_map.setdefault(edge[2], [])
            color_map[edge[2]].append(edge)
            _ = vertex_map.setdefault(edge[0], [])
            vertex_map[edge[0]].append(edge[2])
            _ = vertex_map.setdefault(edge[1], [])
            vertex_map[edge[1]].append(edge[2])
        
        self.tipo_trilha = {}
        for color, edges in color_map.items():
            self.tipo_trilha[color] = self._definir_tipo_trilha(Graph(edges))

        grafo_auxiliar = [0] * 9
        for colors in vertex_map.values():
            x = set([color for color in colors if colors.count(color) > 1])
            trails = self.tipo_trilha[x.pop()] + self.tipo_trilha[x.pop()]
            if trails == '00':
                continue
            grafo_auxiliar[self._get_color_obs_position(trails)] += 1

        return np.array(grafo_auxiliar) # MlpPolicy
        # return {"trails": np.array(grafo_auxiliar)} # MultiInputPolicy

    def _observation_space(self):
        states = Box(-np.inf, np.inf, shape=(1, 64,), dtype=np.float32)
        return states

    def _actions_space(self):
        '''
        qual tipo vou trocar com o outro tipo;
        dá uma recompensa proporcional ao número de opções de trocas desse tipo;
        '''

        '''
        qual subgrafo os dois elementos 

        grafo dos dois elementos após as trocas
        '''

        '''
        dicionario de uma troca:
        pra quais elementos uma troca em cada par de elementos pode levar
        ex: T3 com T3 pode virar um T2 e um T1
        '''
        # return MultiDiscrete([4, 4, 4, 4])
        # return MultiDiscrete([37])
        # return Discrete(37) # repeat
        # return Discrete(34) # alguns planares
        # return Discrete(27) # K6
        return Discrete(57) # 8, 10 e 12 vértices

    def _get_graph_initial_dec(self):
        random_matching = randint(0, max_perfect_matchings)
        random_graph = randint(0, len(self.graph_list) - 1)
        # random_graph = 2
        # random_matching = 4
        print("*"*100)
        print("random_matching: ", random_matching, "random_graph: ", random_graph)
        G = Graph(self.graph_list[random_graph])
        cont = 0
        for M in G.perfect_matchings():
            if cont < random_matching:
                cont += 1
                continue
            for i in M:
                G.delete_edge(i)
            petersen = G.two_factor_petersen()
            for i in M:
                G.add_edge(i)
            H = Graph(G)
            # start_time = time.time()
            H, _ = canonicalDecomposition(H, M, petersen)
            break
        return H

    def reset(self, seed = None, options = None, current_graph = None):
        if current_graph:
            self.current_graph = current_graph
            self.possible_moves, self.hanging_edges_status, _ = self._get_possible_moves()
        else:
            hanging_edges_status = True
            while hanging_edges_status:
                self.current_graph = self._get_graph_initial_dec()
                self.possible_moves, hanging_edges_status, _ = self._get_possible_moves()
        self.step_counter = 0
        self.cont_invalid = 0
        # self._show()
        # self._reset_prev_observation()
        # observation = self._get_obs()
        # self.prev_observation.append(observation)
        observation = self._get_gnn_embeddings()  # Calcula os embeddings com a GNN
        return observation, {}


    def _get_action_mapping(self, action):
        mapping = {
            1: '0100', 
            2: '0102', 
            3: '0122', 
            4: '0200', 
            5: '0201', 
            6: '0202', 
            7: '2201',
        }
        mapping = {
            1: [['01', '10'], ['00']],
            2: [['01', '10'], ['02', '20']],
            3: [['01', '10'], ['22']],
            4: [['02', '20'], ['00']],
            5: [['02', '20'], ['01', '10']],
            6: [['02', '20'], ['02', '20']],
            7: [['22'], ['01', '10']],
        }
        return mapping[action]

    def _definir_tipo_trilha(self, T):
        tamanho_trilha = len(T)
        cintura_trilha = T.girth()
        if tamanho_trilha == 4:
            return '3'
        elif tamanho_trilha == 6 and max(T.degree()) == 2:
            return '0'
        elif cintura_trilha == 4:
            return '1'
        elif cintura_trilha == 3:
            return '2'
        return None

    def _definir_tipo_trilha_int(self, T) -> int:
        tamanho_trilha = len(T)
        cintura_trilha = T.girth()
        if tamanho_trilha == 4:
            return 3
        elif tamanho_trilha == 6 and max(T.degree()) == 2:
            return 0
        elif cintura_trilha == 4:
            return 1
        elif cintura_trilha == 3:
            return 2
        return None

    def _get_obs(self):
        """
        Temos dois dicionários, um de cores, onde cada chave é uma cor e o valor é uma lista com as arestas daquela cor.
        Um de vértices, tendo vértices como chaves e uma lista de cor que o vértice está colorido.

        Para toda aresta:
            preenchemos os dicionários de cores e vértices.

        Para cada cor, verificamos qual tipo de trilha ela representa.

        Geramos uma lista (grafo auxiliar) todo preenchido com zero.

        para cada véritice: 
            identificamos os tipos de trilhas que passam por ele (e tem grau maior que 1)
            incrementamos o valor na posição correspondente
        """
        edges_list = self.current_graph.edges()
        color_map = {}
        vertex_map = {}
        for edge in edges_list:
            _ = color_map.setdefault(edge[2], [])
            color_map[edge[2]].append(edge)
            _ = vertex_map.setdefault(edge[0], [])
            vertex_map[edge[0]].append(edge[2])
            _ = vertex_map.setdefault(edge[1], [])
            vertex_map[edge[1]].append(edge[2])
        
        self.tipo_trilha = {}
        for color, edges in color_map.items():
            self.tipo_trilha[color] = self._definir_tipo_trilha(Graph(edges))

        grafo_auxiliar = [0] * 9
        for colors in vertex_map.values():
            x = set([color for color in colors if colors.count(color) > 1])
            trails = self.tipo_trilha[x.pop()] + self.tipo_trilha[x.pop()]
            if trails == '00':
                continue
            grafo_auxiliar[self._get_color_obs_position(trails)] += 1

        return np.array(grafo_auxiliar) # MlpPolicy
        # return {"trails": np.array(grafo_auxiliar)} # MultiInputPolicy

    def _get_possible_moves_colors(self):
        possible_colors = []
        for possible_move in self.possible_moves:
            possible_colors_obs = []
            possible_colors_obs_inverter = []
            for move_edge in possible_move:
                possible_colors_obs.append(move_edge[2])
                possible_colors_obs_inverter.insert(0, move_edge[2])
            possible_colors.append(np.array(possible_colors_obs))
            possible_colors.append(np.array(possible_colors_obs_inverter))
        return possible_colors

    def reward(self, is_valid_move, is_old_observation, hanging_edges_status, cont, moves_possibles):
        '''
        recompensa pelo numero de caminhos
        recompensa maior se o número de ações for menor
        resolveu bom recompensa grande positiva
        resolveu mal recompensa grande negativa

        diminuir o número de hangging edges
        -> recompensa boa é a variação do número de hangging edges, diminuiu mais o número de arestas pendentes. Resolve mais os elementos
        '''
        if hanging_edges_status:
            return 1000 * self.element_number
        if len(self.possible_moves) == 0 or len(moves_possibles) == 0 or self.cont_invalid > 10:
            return -1000 * self.element_number
        if not is_valid_move:
            return -10
        # return 0 # TODO: pensar numa recompensa intermediária
        if is_old_observation:
            return -100
        if self.step_counter > 15:
            return -100
        # return 1 / (len(self.actions) or 1)
        return self.nodes_number / cont


    def _is_valid_move(self, action_index) -> bool:
        action = self.mapping_action[action_index]
        counter_moves_possibles = 0
        for possible_move in self.possible_moves:
            first_condition = (self.tipo_trilha[possible_move[0][2]] == action[0]) and (self.tipo_trilha[possible_move[1][2]] == action[1])
            second_condition = (self.tipo_trilha[possible_move[0][2]] == action[1]) and (self.tipo_trilha[possible_move[1][2]] == action[0])
            if first_condition or second_condition:
                self._move(possible_move)
                edges = extractColor(self.current_graph, possible_move[0][2])
                t1 = self._definir_tipo_trilha(Graph(edges))
                edges = extractColor(self.current_graph, possible_move[1][2])
                t2 = self._definir_tipo_trilha(Graph(edges))
                first_condition = (t1 == action[2]) and (t2 == action[3])
                second_condition = (t1 == action[3]) and (t2 == action[2])
                if first_condition or second_condition:
                    return True, []
                else:
                    counter_moves_possibles += 1
                    self._unmove(possible_move)
            else:
                counter_moves_possibles += 1
        return False, [] if counter_moves_possibles == 0 else [None]

    def _move(self, movement):
        move(self.current_graph, movement)

    def _unmove(self, movement):
        unmove(self.current_graph, movement)

    def _get_possible_moves(self):
        hanging_edges, hanging_edges_status, cont = takeHangingEdges_v2(self.current_graph)
        return possibleMoves(self.current_graph, hanging_edges), hanging_edges_status, cont

    def _get_pair_from_action_box(self, action):
        if action[0][0] > action[0][1]:
            aux = action[0][0]
            action[0][0] = action[0][1]
            action[0][1] = aux
        
        if action[1][0] > action[1][1]:
            aux = action[1][0]
            action[1][0] = action[1][1]
            action[1][1] = aux
        return [tuple(action[0]), tuple(action[1])]
    
    def _get_pair_from_action_multi_discrete(self, action):
        if action[0] > action[1]:
            aux = action[0]
            action[0] = action[1]
            action[1] = aux
        
        if action[3] > action[4]:
            aux = action[3]
            action[3] = action[4]
            action[4] = aux
        return [(action[0], action[1], action[2]), (action[3], action[4], action[5])]

    def _get_move_from_action(self, action):
        for possible_move in self.possible_moves:
            first_condition = possible_move[0][2] == action[0] and possible_move[1][2] == action[1]
            second_condition = possible_move[0][2] == action[1] and possible_move[1][2] == action[0]
            if first_condition or second_condition:
                return possible_move

        

    def step(self, action):
        self.possible_moves, hanging_edges_status, cont = self._get_possible_moves()
        is_valid_move, moves_possibles  = self._is_valid_move(action)
        is_old_observation = False
        self.step_counter += 1
        if is_valid_move:
            # move = self._get_move_from_action(action)
            # self._move(move)
            # self._show()
            print("Invalid cont: ", self.cont_invalid)
            self.cont_invalid = 0

            self.possible_moves, hanging_edges_status, cont = self._get_possible_moves()
        else:
            self.cont_invalid += 1

        # reward = self.reward(is_valid_move, is_old_observation, hanging_edges_status, cont, moves_possibles)
        # return observation, reward, self.terminal(moves_possibles or self.possible_moves, is_old_observation, hanging_edges_status), False, {}
        reward = self.reward(is_valid_move, is_old_observation, hanging_edges_status, cont, [None])
        return self._get_gnn_embeddings(), reward, self.terminal(self.possible_moves, hanging_edges_status, is_old_observation), False, {}

    # def step(self, action):
    #     return self._get_obs(), 1, True, False, {}

    def terminal(self, possible_moves, hanging_edges_status, is_old_observation):
        if hanging_edges_status:
            print("!"*100)
            print("GANHOU!")
            print("*"*100)
        return hanging_edges_status or len(possible_moves) == 0 or is_old_observation or self.cont_invalid > 10 or self.step_counter > 20

    def render(self, mode='human'):
        print(f"Estado atual: {self._get_gnn_embeddings()}")