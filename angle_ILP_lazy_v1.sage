"""
    Implementa PLI por angulos com condições adicionadas via callback (em tempo de execução do solver)
"""

import gurobipy as gp
import psutil 
import time
import os
from gurobipy import GRB

def pair_to_angle(pair):
    """
        Retorna uma tupla com os pares ordenados de uma lista;
    """
    pair.sort()
    return (pair[0], pair[1])

def angle_to_common_vertex(angle):
    """
        Retorna o vértice em comum entre dois ângulos;
    """
    u, v, _ = angle[0]
    x, y, _ = angle[1]
    if u == x or u == y:
        return u
    else:
        return v


# ACHO QUE DA PRA GENERLIZAR AS TRES FUNÇÔES ABAIXO EM UMA SÓ!!!
def edge_to_other_vertex(edge, vertex):
    """
        Retorna o outro vértice de uma aresta;
    """
    if vertex == edge[0]:
        return edge[1]
    else:
        return edge[0]


def angle_to_other_edge(angle, edge):
    """
        Retorna a outra aresta de um ângulo;
    """
    if edge == angle[0]:
        return angle[1]
    else:
        return angle[0]


def pair_to_other(pair, sample):
    """
        Retorna o outro par;
    """
    if sample == pair[0]:
        return pair[1]
    else:
        return pair[0]



def mycallback(model, where):
    """
    This function checks whether the incumbent solution found by Gurobi has a
    cycle or not. If a cycle was found, then this function adds a constraint
    that is violated by the current solution.

    To be more precise, if a cycle C is found in the current solution,
    then this function adds the following constraint

      ∑ x_{e, 0} ≤ |E(C)| - 1
    e ∈ E(C)
    """

    if where == GRB.Callback.MIPSOL:

        if model._cont % 100 == 0:
            percentage_used_memory = psutil.virtual_memory()[2]
            print("memória usada: ", percentage_used_memory)
            if percentage_used_memory > 76:
                model._break_type = 'memory'
                model.terminate()

        if model._cont > 10000:
            model._break_type = 'iteration'
            model.terminate()

        vals = model.cbGetSolution(model._x)

        model._cont += 1

        cycles, paths = solution_cycles(vals, 5, model._G)

        for c in cycles:
            model.cbLazy(cycle_constraint_extended(c, model._x) <= len(c) - 3)
        for path in paths:
            #aqui setei (2k+1) = 5
            model.cbLazy(path_constraint(path, model._x) <= 4)
        
        model.update()


# DÌVIDA!!!
def solution_cycles(solution, k, G):
    """
        A disjoint-set data structure (sometimes called union-find data structure) is a data structure 
            that keeps track of a partitioning of a set into a number of separate, nonoverlapping sets. 
            It performs two operations:
                find() – Determine which set a particular element is in.
                union() – Combine or merge two sets into a single set.
        ;

        inicialmete temos:
            - M grupos, um pra cada aresta;  
            - Um dicionário dic com M chaves, com listas contendo False;
            - uma lista vazia de ângulos setados
        E para cada ângulo setado na solução:
            - unimos os grupos das arestas dos ângulos
            - adicionamos o ângulos na lista de ângulos setados
            - adicionamos nas listas das arestas que compõem o ângulo o objeto setted (ângulo)

        # definir sequências
        sequências são trilhas geradas pelos ângulos setados;

        paths é uma lista de sequências que não repete vértice e tem tamanho maior que k+1

        cycles é uma lista de sequências que repete vértice, partindo do vértice repetido e finalizando no vértice repetido

    """
    disjointSet = DisjointSet(G.edges())
    setted_angles = []
    dic = {}
    for e in G.edges():
        dic[e] = [False]
    for setted in solution:
        if solution[setted] >= 0.5:
            disjointSet.union(setted[0], setted[1])
            setted_angles.append(setted)
            dic[setted[0]].append(setted)
            dic[setted[1]].append(setted)
    
    '''
    # antigo com "conflito" no "e"
    sequences = []
    for e in dic:
        if len(dic[e]) == 2 and dic[e][0] == False:
            dic[e][0] = True
            angle = dic[e][1]
            common_vertex = angle_to_common_vertex(angle)
            initial_vertex = edge_to_other_vertex(e, common_vertex)
            new_sequence = [initial_vertex, common_vertex]
            e = angle_to_other_edge(angle, e)
            while len(dic[e]) == 3:
                dic[e][0] = True
                new_vertex = edge_to_other_vertex(e, new_sequence[-1])
                new_sequence.append(new_vertex)
                pair = [dic[e][1], dic[e][2]]
                angle = pair_to_other(pair, angle)
                e = angle_to_other_edge(angle, e)
                print(f'entrei no while, que acho que não entra, {e}')
            dic[e][0]=True
            new_vertex = edge_to_other_vertex(e, new_sequence[-1])
            new_sequence.append(new_vertex)
            sequences.append(new_sequence)

    for e in dic:
        if dic[e][0] == False:
            dic[e][0] = True
            angle = dic[e][1]
            common_vertex = angle_to_common_vertex(angle)
            initial_vertex = edge_to_other_vertex(e, common_vertex)
            new_sequence = [initial_vertex, common_vertex]
            e = angle_to_other_edge(angle, e)
            while dic[e][0] == False:
                dic[e][0] = True
                new_vertex = edge_to_other_vertex(e, new_sequence[-1])
                new_sequence.append(new_vertex)
                pair = [dic[e][1], dic[e][2]]
                angle = pair_to_other(pair, angle)
                e = angle_to_other_edge(angle, e)
            sequences.append(new_sequence)
    '''
    sequences = []
    for i in dic:
        if len(dic[i]) == 2 and dic[i][0] == False:
            dic[i][0] = True
            angle = dic[i][1]
            common_vertex = angle_to_common_vertex(angle)
            initial_vertex = edge_to_other_vertex(i, common_vertex)
            new_sequence = [initial_vertex, common_vertex]
            e = angle_to_other_edge(angle, i)
            while len(dic[e]) == 3:
                dic[e][0] = True
                new_vertex = edge_to_other_vertex(e, new_sequence[-1])
                new_sequence.append(new_vertex)
                pair = [dic[e][1], dic[e][2]]
                angle = pair_to_other(pair, angle)
                e = angle_to_other_edge(angle, e)
                #print(f'entrei no while, que acho que não entra, {e}')
            dic[e][0] = True
            new_vertex = edge_to_other_vertex(e, new_sequence[-1])
            new_sequence.append(new_vertex)
            sequences.append(new_sequence)

    for i in dic:
        if dic[i][0] == False:
            dic[i][0] = True
            angle = dic[i][1]
            common_vertex = angle_to_common_vertex(angle)
            initial_vertex = edge_to_other_vertex(i, common_vertex)
            new_sequence = [initial_vertex, common_vertex]
            e = angle_to_other_edge(angle, i)
            while dic[e][0] == False:
                dic[e][0] = True
                new_vertex = edge_to_other_vertex(e, new_sequence[-1])
                new_sequence.append(new_vertex)
                pair = [dic[e][1], dic[e][2]]
                angle = pair_to_other(pair, angle)
                e = angle_to_other_edge(angle, e)
            sequences.append(new_sequence)

    count = []
    cycles = []
    paths = []
    position = []
    # gerando listas auxiliares
    for v in G.vertices():
        count.append(0)
        position.append(-1)

    for sequence in sequences:
        v = sequence[0]
        pos = 0
        isPath = True
        for v in sequence:
            if count[v] == 0:
                position[v] = pos
            else:
                cycle = []
                isPath = False
                for u in range(position[v], pos+1):
                    cycle.append(sequence[u])
                cycles.append(cycle)
                position[v] = pos
            count[v] += 1
            pos += 1
        if (isPath == True and len(sequence) > (k+1)):
            paths.append(sequence)
        
        # limpando
        for u in G.vertices():
            count[u] = 0
            position[u] = -1

    return cycles, paths


# dúvida, como é formado o ciclo? o primeiro vértice também é o último?
def cycle_constraint_extended(cycle, w):
    """
        Dado os vértices (v1,v2,v3,...,vk) de um ciclo e as variáveis do PLI (w), 
        retorna uma condição com todos os ângulos que compõem o ciclo;
    """
    angles = cycle_to_angles(cycle)
    constraint = 0
    for angle in angles:
        constraint = constraint + w[angle]
    return constraint


def path_constraint(vertices, w):
    """
        Dado os vértices (v1,v2,v3,...,vk) de um caminho e as variáveis do PLI (w), 
        retorna uma condição com todos os ângulos que compõem o caminho;
    """
    constraint = 0
    l = len(vertices)
    for i in range(0, l - 2):
        edge1 = pair_to_edge([vertices[i], vertices[i+1]])
        edge2 = pair_to_edge([vertices[i+1], vertices[i+2]])
        angle = pair_to_angle([edge1, edge2])
        constraint = constraint + w[angle]
    return constraint


def pair_to_edge(pair):
    """
        Dado dois vértice, 
        retorna no formato de aresta onde o primeiro está na primeira posição da tupla 
            e o segundo na segunda posição;
    """
    pair.sort()
    return (pair[0],pair[1],None)


def cycle_to_angles(cycle):
    """
        Dado um ciclo, 
        retorna todos os ângulos que compõem o ciclo;
    """
    angles = []
    for i in range(0, len(cycle) - 2):
        u = cycle[i]
        v = cycle[i+1]
        w = cycle[i+2]
        edge1 = pair_to_edge([u, v])
        edge2 = pair_to_edge([v, w])
        angle = pair_to_angle([edge1, edge2])
        angles.append(angle)
    u = cycle[-2]
    v = cycle[0]
    w = cycle[1]
    edge1 = pair_to_edge([u, v])
    edge2 = pair_to_edge([v, w])
    angle = pair_to_angle([edge1, edge2])
    angles.append(angle)
    return angles


class Model: #(gp.Model):

    def __init__(self, G):
        self.model = gp.Model("5-path decomposition")
        self.model.setParam('OutputFlag', 0)
        
        self.G = G
        self.model._cont = 0
        self.model._break_type = None
        self._init_x_variables()

        # The next lines are defining some variables inside the model object so
        # that they can be accessed in the callback (yeah.. I'm breaking
        # encapsulation).  That's not very pretty, but it's the way it's
        # suggested by the Gurubi Another solution would be to define global
        # variables.
        self.model._x = self.x
        self.model._G = self.G

        self._add_constr_vertex_degree()
        self._add_constr_one_color_to_each_edge()


    def _init_x_variables(self):
        """
              ⎧1,  if e ∈ E(G) is selected
        x_e = ⎨
              ⎩0,  otherwise
        """
        vertices = self.G.vertices()
        indices = []
        for v in vertices:
            iterator = Subsets(self.G.edges_incident(v), 2)
            for pair in iterator:
                angle = pair_to_angle([pair[0], pair[1]])
                indices.append(angle)

        self.x = self.model.addVars(indices, lb=0.0, ub=1.0, vtype=GRB.BINARY, name="x")
        self.model.update()


    def _add_constr_vertex_degree(self):
        """
        ### AJUSTAR Every vertex has at degree at most 2, and 0 has degree precisely 1
        """
        vertices = self.G.vertices()
        for v in vertices:
            equation = 0
            iterator = Subsets(self.G.edges_incident(v), 2)
            for pair in iterator:
                angle = pair_to_angle([pair[0], pair[1]])
                equation += self.x[angle]
            _ = self.model.addConstr(equation == floor(self.G.degree(v)/2), name='c1')

        self.model.update()


    def _add_constr_one_color_to_each_edge(self):
        """
        Every vertex has at degree at most 2, and 0 has degree precisely 1
        """

        edges = self.G.edges()
        for e in edges:
            edge_must_be_in_angle = 0
            for cont in range(2):
                constraint = 0
                incident = self.G.edges_incident(e[cont])
                for i in incident:
                    if (e != i):
                        angle = pair_to_angle([e, i])
                        constraint += self.x[angle]
                        edge_must_be_in_angle += self.x[angle]
                _ = self.model.addConstr(constraint <= 1, name='c2')
            _ = self.model.addConstr(edge_must_be_in_angle >= 1, name='c3')
        self.model.update()


    def solve(self):

        # self.model.write("modelo_debug.lp")

        # ⚠ if you plan to use lazyConstraints in Gurobi,
        #     you must set the following parameter to 1
        self.model.Params.lazyConstraints = 1

        # to use an lazyConstraint `foo`, you must pass it
        # as a parameter in the function optimize
        self.model.optimize(mycallback)

    # getter method
    def get_cont(self):
        return self.model._cont

    def get_break_type(self):
        return self.model._break_type

    @property
    def cont(self):
        return self.model._cont


def set_angle_model(G):
    start_time = time.time()
    m = Model(G)
    status = True
    middle_time = time.time()
    total_memory, used_memory, _ = map(int, os.popen('free -t -m').readlines()[-1].split()[1:]) 
    print("RAM memory % used:", used_memory/total_memory)
    if used_memory/total_memory < 0.71:
        try:
            m.solve()
        except:
            status = False
        final_time = time.time()
        contador = m.get_cont()
        break_type = m.get_break_type()
        if break_type == 'iteration':
            print('iteration')
            status = None 
        elif break_type == 'memory':
            print('memory')
            status = None 
    else:
        final_time = time.time()
        status = None
        contador = -1
    return [G.graph6_string(), middle_time - start_time, final_time - middle_time, status, contador, break_type]