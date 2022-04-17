import gurobipy as gp
from gurobipy import GRB


# PENSAR MELHOR AQUI
## IDEIA 
### dado os angulos setados, selecionar quais precisamos criar restrições, pois não atendem ao problema


def is_path_of_length_five(edges):
    X = Graph(edges)
    for H in X.connected_components_subgraphs(): 
        # H = Graph(edges)
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

        vals = model.cbGetSolution(x)

        dic = {}
        print(numero_de_cores)
        for c in range(numero_de_cores):
            dic[c] = []
            
        for (triple, val) in vals.items():
            if val > 0:
                u, v, c = triple
                dic[c].append((u, v, c))
        
        for c in range(numero_de_cores):
            edges = dic[c]
            #print(is_path_of_length_five(edges))
            if not is_path_of_length_five(edges):
                equation = 0
                for e in edges:
                    u, v, c = e
                    equation += x[u, v, c]
                model.cbLazy(equation <= 4)
        model.update()
        print(model)


        for c in cycles:
            p.add_constraint(cycle_constraint_extended(c, w) <= len(c)-3)
        for path in paths:
            #aqui setei (2k+1) = 5
            p.add_constraint(path_constraint(path, w) <= 4)
        p.solve()
        print(p)
        cont_numb_of_solves+=1
        if cont_numb_of_solves%100==0:
            print(cont_numb_of_solves)
            print(p)
        solution = p.get_values(w).items()
        cycles, paths = solution_cycles(solution, 5)
        #print str(cycles) + " ? " + str(paths)
        if cycles == [] and paths == []:
            noCyclesNPaths = True