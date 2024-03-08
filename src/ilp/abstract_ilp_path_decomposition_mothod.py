import time
import gurobipy as gp
from sage.all import *

class AbstractIlpPathDecompositionMothod():
    def __init__(self, G) -> None:
        self._graph = Graph(G)
        self._start_graph = Graph(G)
        self._n = self._graph.order()

    def _set_model(self):
        self.model = gp.Model("5-path decomposition")
        self.model.setParam('OutputFlag', 0)

        self.model._cont = 0
        self.model._break_type = None
        self._init_x_variables()
        self.model.Params.lazyConstraints = 1


    def _init_x_variables(self):
        pass

    def _add_constraints(self):
       pass


    def _my_callback(self, model, where):
        pass

    def solve(self):
        self.model.optimize(self._my_callback)

    def run(self):
        pass

    # getter method
    def get_cont(self):
        return self.model._cont

    def get_break_type(self):
        return self.model._break_type

    @property
    def cont(self):
        return self.model._cont