
import time
from sage.all import *
from gnn.env import GraphDecompositionEnv
from brute.path_decomposition import PathDecomposition
from gnn.utils import canonicalDecomposition
from sb3_contrib import MaskablePPO

class GNNPathDecompositionMothod(PathDecomposition):
    def __init__(self, G) -> None:
        self._graph = Graph(G)
        self._start_graph = Graph(G)
        self._n = self._graph.order()
        models_dir = f"gnn/models"
        # self.model_path = f"{models_dir}/3490000_planeres"
        self.model_path = f"{models_dir}/GNN-1727454260"

    def _load_model(self, H):
        self.env = GraphDecompositionEnv(5, H)
        self.model = MaskablePPO.load(self.model_path, env=self.env)

    def _get_petersen(self, perfect_matching):
        H = Graph(self._start_graph)
        H.delete_edges(perfect_matching)
        return H.two_factor_petersen()

    def _run_model(self, perfect_matching, petersen):
        self._graph = Graph(self._start_graph)
        start_time = time.time()
        _ = self.set_canonical_decomposition(perfect_matching, petersen)
        middle_time = time.time()
        
        self._load_model(self._graph)
        obs, _ = self.env.reset(current_graph=self._graph)
        done = False
        moves = 0
        while not done:
            valid_action_array = self.env.action_masks()
            action, _state = self.model.predict(obs, action_masks=valid_action_array)
            moves += 1
            obs, reward, done, info, _ = self.env.step(action)
        final_time = time.time()

        return [self._start_graph.graph6_string(), str(list(perfect_matching)).replace(",","-"), middle_time - start_time, final_time - middle_time, moves, self.env.hanging_edges_status, 0]

    def run(self, perfect_matching_limit = 10):
        print('GNN')
        result = []
        limit_counter = 0
        for perfect_matching in self._start_graph.perfect_matchings():
            petersen = self._get_petersen(perfect_matching)
            result.append(self._run_model(perfect_matching, petersen))

            petersen_reverse = [petersen[1], petersen[0]]
            result.append(self._run_model(perfect_matching, petersen_reverse))

            limit_counter += 1
            if limit_counter >= perfect_matching_limit:
                return result
        return result

    def run_simgle_matching(self):
        print('GNN')
        result = []
        perfect_matching = self._start_graph.matching()
        petersen = self._get_petersen(perfect_matching)
        result.append(self._run_model(perfect_matching, petersen))

        petersen_reverse = [petersen[1], petersen[0]]
        result.append(self._run_model(perfect_matching, petersen_reverse))

        return result
