import time
from sage.all import *
from path_decomposition import PathDecomposition

class BrutePathDecompositionMothod():
    def __init__(self, G, path_decomposition_functions: PathDecomposition = PathDecomposition) -> None:
        self._graph = Graph(G)
        self._start_graph = Graph(G)
        self._n = self._graph.order()
        self._path_decomposition_functions = path_decomposition_functions()


    def _search_s2(self, hanging_edges, hanging_edges_status, movements=[], old_decompositions=[], max_depth=[]):
        # recursion that runs through the graph until it finds a path decomposition
        # returns (moves, True) if it finds, otherwise (moves, False)
        # Retorna em moves a profundidade da solução
        if (hanging_edges_status == True):
            return movements, True, max_depth
        possible_moves = self._path_decomposition_functions.get_possible_moves(hanging_edges)
        solved = False
        graph_aux = Graph(self._graph)
        old_decompositions.append(graph_aux.edges())
        if len(old_decompositions) >= 100:
            return movements, solved, max_depth
        for i in possible_moves:
            self._path_decomposition_functions.make_move(i)
            dec = self._graph.edges()
            if (dec not in old_decompositions):
                hanging_edges, hanging_edges_status = self._path_decomposition_functions.take_hanging_edges()
                movements.append(i)
                max_depth.append(len(movements))
                if (hanging_edges_status == True):
                    return movements, True, max_depth
                movements, solved, max_depth = self._search_s2(hanging_edges, hanging_edges_status, movements, old_decompositions, max_depth)
                if (solved==True):
                    return movements, solved, max_depth
                else:
                    _ = movements.pop()
            self._path_decomposition_functions.make_unmove(i)
        return movements, solved, max_depth


    def _do_the_search(self, perfect_matching, petersen):
        self._graph = Graph(self._start_graph)
        start_time = time.time()
        _ = self._path_decomposition_functions.set_canonical_decomposition(perfect_matching, petersen)
        middle_time = time.time()
        hangingEdges, hangingEdgesStatus = self._path_decomposition_functions.take_hanging_edges()
        moves, status, depth = self._search_s2(hangingEdges, hangingEdgesStatus, [], [], [])
        final_time = time.time()
        if depth == []:
            max_depth = 0
        else:
            max_depth = max(depth)
        return [self._start_graph.graph6_string(), str(list(perfect_matching)).replace(",","-"), middle_time - start_time, final_time - middle_time, len(moves), status, max_depth]


    def run(self, perfect_matching_limit = 10):
        print('Brute Force')
        result = []
        limit_counter = 0
        for perfect_matching in self._start_graph.perfect_matchings():
            petersen = self._path_decomposition_functions.get_petersen(perfect_matching)
            result.append(self._do_the_search(perfect_matching, petersen))

            petersen_reverse = [petersen[1], petersen[0]]
            result.append(self._do_the_search(perfect_matching, petersen_reverse))

            limit_counter += 1
            if limit_counter >= perfect_matching_limit:
                return result
        return result


    def check_canonical_done(self):
        perfect_matching_counter = 0
        for perfect_matching in self._start_graph.perfect_matchings():
            start_time = time.time()
            petersen = self._path_decomposition_functions.get_petersen(perfect_matching)
            self._graph = Graph(self._start_graph)
            _ = self._path_decomposition_functions.set_canonical_decomposition(perfect_matching, petersen)
            hangingEdges, hangingEdgesStatus = self._path_decomposition_functions.take_hanging_edges()
            middle_time = time.time()
            moves, status, depth = self._search_s2(hangingEdges, hangingEdgesStatus, [], [], [])
            final_time = time.time()
            if status == True:
                return status, [final_time - start_time, final_time - middle_time, perfect_matching_counter]
            perfect_matching_counter += 1
        return status, [final_time - start_time, final_time - middle_time, perfect_matching_counter]
