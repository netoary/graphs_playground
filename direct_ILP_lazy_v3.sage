# https://www.gurobi.com/documentation/9.5/examples/mip1_py.html#subsubsection:mip1.py
# https://www.linkedin.com/pulse/como-utilizar-fun%C3%A7%C3%A3o-callback-gurobi-igor-gir%C3%A3o

#!/bin/env sage
# -*- coding: utf-8 -*-
import gurobipy as gp
from gurobipy import GRB

def is_path_of_length_five(edges):
    H = Graph(edges)
    if not H.is_connected():
        return False
    if not H.is_forest():
        return False
    return True

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
        print("entrou no callback")

        vals = model.cbGetSolution(model._x)

        dic = {}
        print(model._numero_de_cores)
        for c in range(model._numero_de_cores):
            dic[c] = []
            
        for (triple, val) in vals.items():
            if val > 0:
                u, v, c = triple
                dic[c].append((u, v, c))
        
        
        for c in range(model._numero_de_cores):
            edges = dic[c]
            print(is_path_of_length_five(edges))
            if not is_path_of_length_five(edges):
                equation = 0
                for e in edges:
                    u, v, c = e
                    equation += model._x[u, v, c]
                model.cbLazy(equation <= 4)
        model.update()
        

class Model: #(gp.Model):

    def __init__(self, G):
        self.model = gp.Model("5-path decomposition")
        self.model.setParam('OutputFlag', 0)
        
        self.G = G
        self.model._numero_de_cores = G.size()/5
        self._init_x_variables()

        # The next lines are defining some variables inside the model object so
        # that they can be accessed in the callback (yeah.. I'm breaking
        # encapsulation).  That's not very pretty, but it's the way it's
        # suggested by the Gurubi Another solution would be to define global
        # variables.
        self.model._x = self.x
        self.model._G = self.G

        self._add_constr_vertex_degree()
        self._add_constr_number_of_edges_of_each_color()


    def _init_x_variables(self):
        """
              ⎧1,  if e ∈ E(G) is selected
        x_e = ⎨
              ⎩0,  otherwise
        """
        indices = [(u, v, c) for u, v, label in self.G.edges() for c in range(self.model._numero_de_cores)]
        self.x = self.model.addVars(indices, lb=0.0, ub=1.0, vtype=GRB.BINARY, name="x")
        self.model.update()


    def _add_constr_vertex_degree(self):
        """
        Every vertex has at degree at most 2, and 0 has degree precisely 1
        """
        for u in self.G.vertices():
            for c in range(self.model._numero_de_cores):
                equation = 0
                for e in self.G.edges_incident(u):
                    a, b, _ = e
                    equation += self.x[a, b, c]
                
                self.model.addConstr(equation<=2, name='each color has maximum degree at most 2')
        self.model.update()


    def _add_constr_number_of_edges_of_each_color(self):
        """
        Every vertex has at degree at most 2, and 0 has degree precisely 1
        """
        for c in range(self.model._numero_de_cores):
            equation = 0
            for e in self.G.edges():
                a, b, _=e
                equation += self.x[a, b, c]

            self.model.addConstr(equation==5, name='each color has five edges')
        self.model.update()


    def _add_constr_one_color_to_each_edge(self):
        """
        Every vertex has at degree at most 2, and 0 has degree precisely 1
        """
        for e in self.G.edges():
            equation = 0
            a, b, _ = e
            for c in range(self.model._numero_de_cores):
                equation += self.x[a, b, c]

            self.model.addConstr(equation==1, name='each edge has one color')
        self.model.update()


    def solve(self):

        self.model.write("modelo_debug.lp")

        # ⚠ if you plan to use lazyConstraints in Gurobi,
        #     you must set the following parameter to 1
        self.model.Params.lazyConstraints = 1

        # to use an lazyConstraint `foo`, you must pass it
        # as a parameter in the function optimize
        self.model.optimize(mycallback)

    def show(self):

        if self.model.status != GRB.OPTIMAL:
            return []

        edges=[]
        for e in self.G.edges():
            u,v,label=e
            for c in range(self.model._numero_de_cores):
                if self.x[u,v,c].x >0.1:
                    G.set_edge_label(u,v,c)
        G.show(color_by_label=True, layout="circular")

#G=graphs.RandomRegular(5,10)
#m = Model(G)
#m.solve()
#m.show()