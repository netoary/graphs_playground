from sage.all import *

class PathDecomposition():
    def __init__(self, graph: str) -> None:
        self._graph = Graph(graph)
        self._start_graph = Graph(graph)
        self._n = self._graph.order()


    def get_petersen(self, perfect_matching):
        H = Graph(self._start_graph)
        H.delete_edges(perfect_matching)
        return H.two_factor_petersen()


    def set_canonical_decomposition(self, perfect_matching = [], petersen = []):
        # If graph does not have perfect matching the function returns original graph, "False"
        # petersen is a list of 2-factors without M, which is a graph matching
        # For each edge in a 2-factor its label is changed
        # If for each matching of M a trail is generated (identified by the labels between 0 and (m / r) -1),
        # the function returns colored graph, "True"

        if perfect_matching == []:
            perfect_matching = self._start_graph.matching(algorithm="Edmonds")

        if petersen == []:
            petersen = self.get_petersen(perfect_matching)

        labeling = len(self._graph)
        if (len(perfect_matching) != labeling/2):
            return False

        color = 0
        for i in perfect_matching:
            x = i[0]
            y = i[1]
            self._graph.set_edge_label(x, y, color)
            for k in range(len(petersen)):
                for j in petersen[k]:
                    if (j[0] == x):
                        self._graph.set_edge_label(j[0], j[1], color)
                        x = j[1]
                        break
                for j in petersen[k]:
                    if (j[0] == y):
                        self._graph.set_edge_label(j[0], j[1], color)
                        y = j[1]
                        break
            color += 1
        return True


    def take_hanging_edges(self):
        # tests whether the decomposition is decomposing into paths
        # returns a dictionary with Hanging Edges in each vertex

        hanging_edges = {}
        colors = {}
        edges = self._graph.edges()

        hanging_edges_counter = 0
        for i in range(self._n / 2):
            colors[i] = []
        for i in edges:
            colors[i[2]].append(i)
        for i in colors:
            H = Graph(colors[i])
            for j in H.edges():
                if (mod(H.degree(j[0]), 2) == 1):
                    X = Graph(H)
                    X.delete_edge(j)
                    if (X.is_connected() or H.degree(j[0]) == 1):
                        if (j[1] in hanging_edges):
                            hanging_edges[j[1]].append(j)
                        else:
                            hanging_edges[j[1]] = [j]
                        hanging_edges_counter += 1

                if (mod(H.degree(j[1]), 2) == 1):
                    X = Graph(H)
                    X.delete_edge(j)
                    if (X.is_connected() or H.degree(j[1]) == 1):
                        if (j[0] in hanging_edges):
                            hanging_edges[j[0]].append(j)
                        else:
                            hanging_edges[j[0]] = [j]
                        hanging_edges_counter += 1
        if (hanging_edges_counter == self._n):
            return [], True
        return hanging_edges, False


    def extract_color(self, color):
        # returns a list of the edges that have this color.
        edges = self._graph.edges()
        return [e for e in edges if e[2] == color]


    def get_possible_moves(self, hanging_edges):
        #returns possible moves
        moves = []
        for i in hanging_edges:
            if (len(hanging_edges[i]) >= 2):
                for j in hanging_edges[i]:
                    for k in hanging_edges[i]:
                        if (j[2] != k[2]):
                            trail1=Graph(self.extract_color(j[2]))
                            trail2=Graph(self.extract_color(k[2]))
                            do_they_point_to_degree_1_vertex = (trail1.degree(j[0])==1 or trail1.degree(j[1])==1) and (trail2.degree(k[0]) or trail2.degree(k[1]))
                            if (not([j,k] in moves or [k,j] in moves)) and not do_they_point_to_degree_1_vertex:
                                moves.append([j,k])
        return moves


    def make_move(self, pair):
        #change the label of the pair of edges
        self._graph.set_edge_label(pair[0][0], pair[0][1], pair[1][2])
        self._graph.set_edge_label(pair[1][0], pair[1][1], pair[0][2])


    def make_unmove(self, pair):
        #exchange the label of the pair of edges
        self._graph.set_edge_label(pair[0][0], pair[0][1], pair[0][2])
        self._graph.set_edge_label(pair[1][0], pair[1][1], pair[1][2])
