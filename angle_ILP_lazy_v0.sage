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


def is_path_of_length_five_angles(solution, G):
    disjoint_set = solution_interpreter(solution, G)
    return_list = []
    for i in disjoint_set:
        H = Graph(i)
        if not H.is_connected():
            return_list.append(False)
        elif not H.is_forest():
            return_list.append(False)
        else:
            return_list.append(True)
    return return_list


def solution_interpreter(solution, G):
    disjointSet = DisjointSet(G.edges())
    for setted in solution:
        if setted[1] == 1.0:
            disjointSet.union(setted[0][0],setted[0][1])
    return disjointSet



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


def pair_to_angle(pair):
    """
        Retorna uma tupla com os pares ordenados de uma lista;
    """
    pair.sort()
    return (pair[0], pair[1])


def basic_model(G):
    """
        modelo bese para PLI por algulos;

        variáveis são pares de arestas (os ângulos)
        
        condições:
            - cada vétice só pode ter chão do grau de v sobre dois ângulos setados
            - toda aresta precisa estar em dois ângulos, sendo 1 pra cada vértice da aresta
            - toda aresta precisa estar em pelo menos um ângulo setado
    """
    p = MixedIntegerLinearProgram(maximization=True, solver="GUROBI")
    count = 0
    w = p.new_variable(binary=True)
    dic={}

    vertices = G.vertices()
    for v in vertices:
        constraint = 0
        iterator = Subsets(G.edges_incident(v), 2)
        for pair in iterator:
            angle = pair_to_angle([pair[0], pair[1]])
            constraint = constraint + w[angle]
        p.add_constraint(constraint == floor(G.degree(v)/2))
        # p.add_constraint(constraint <= floor(G.degree(v)/2))
        # p.add_constraint(constraint >= floor(G.degree(v)/2))

    edges = G.edges()
    for e in edges:
        edge_must_be_in_angle = 0
        for cont in range(2):
            constraint = 0
            incident = G.edges_incident(e[cont])
            for i in incident:
                if (e != i):
                    angle = pair_to_angle([e, i])
                    constraint = constraint + w[angle]
                    edge_must_be_in_angle = edge_must_be_in_angle + w[angle]
            p.add_constraint(constraint <= 1)
        p.add_constraint(edge_must_be_in_angle >= 1)
    return p, w

