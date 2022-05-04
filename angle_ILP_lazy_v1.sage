"""
    Implementa PLI por angulos com condições adicionadas via callback (em tempo de execução do solver)
"""

import gurobipy as gp
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
        print("entrou no callback")

        vals = model.cbGetSolution(x)
        print(vals)

        cycles, paths = solution_cycles(vals, 5, G)
        #print(cycles, paths)

        for c in cycles:
            model.cbLazy(cycle_constraint_extended(c, x) <= len(c) - 3)
        for path in paths:
            #aqui setei (2k+1) = 5
            model.cbLazy(path_constraint(path, x) <= 4)
        
        model.update()



G = graphs.RandomRegular(5,10)

model = gp.Model("5-path decomposition")

model.setParam('OutputFlag', 0)

numero_de_cores = G.size()/5

#indices = [pair_to_angle([e1, e2]) for e1 in G.edges() for e2 in range(numero_de_cores) if e1 != e2]

vertices = G.vertices()
indices = []
for v in vertices:
    iterator = Subsets(G.edges_incident(v), 2)
    for pair in iterator:
        angle = pair_to_angle([pair[0], pair[1]])
        indices.append(angle)

x = model.addVars(indices, lb=0.0, ub=1.0, vtype=GRB.BINARY, name="x")

model.update()

vertices = G.vertices()
for v in vertices:
    equation = 0
    iterator = Subsets(G.edges_incident(v), 2)
    for pair in iterator:
        angle = pair_to_angle([pair[0], pair[1]])
        equation += x[angle]
    _ = model.addConstr(equation == floor(G.degree(v)/2), name='c1')

model.update()

edges = G.edges()
for e in edges:
    edge_must_be_in_angle = 0
    for cont in range(2):
        constraint = 0
        incident = G.edges_incident(e[cont])
        for i in incident:
            if (e != i):
                angle = pair_to_angle([e, i])
                constraint += x[angle]
                edge_must_be_in_angle += x[angle]
        _ = model.addConstr(constraint <= 1, name='c2')
    _ = model.addConstr(edge_must_be_in_angle >= 1, name='c3')

model.update()

#model.write("modelo_debug.lp")
model.Params.lazyConstraints = 1
model.optimize(mycallback)



def solution_cycles(solution, k, G):
    """
        ;

        
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

    count = []
    cycles = []
    paths = []
    position = []
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
        for u in G.vertices():
            count[u] = 0
            position[u] =- 1

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