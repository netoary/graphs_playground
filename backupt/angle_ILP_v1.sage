import time


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


def solve_angles_ILP(G):
    """
        chama o modelo base e complementa esse modelo adicionando condições após cada tentativa de solução errada;

        
    """
    inicio = time.time()
    p, w = basic_model(G)
    p.solve()
    solution = p.get_values(w).items()
    #aqui setei (2k+1) = 5
    cycles, paths = solution_cycles(solution, 5, G)
    noCyclesNPaths = False
    if cycles == [] and paths == []:
        noCyclesNPaths = True
    
    cont_numb_of_solves = 0
    while noCyclesNPaths == False:
        for c in cycles:
            p.add_constraint(cycle_constraint_extended(c, w) <= len(c) - 3)
        for path in paths:
            #aqui setei (2k+1) = 5
            p.add_constraint(path_constraint(path, w) <= 4)
        p.solve()
        print(p)
        cont_numb_of_solves += 1
        if cont_numb_of_solves % 100 == 0:
            print(cont_numb_of_solves)
            print(p)
        solution = p.get_values(w).items()
        cycles, paths = solution_cycles(solution, 5, G)
        #print str(cycles) + " ? " + str(paths)
        if cycles == [] and paths == []:
            noCyclesNPaths = True
    
    disjointSet = solution_interpreter(solution)
    cont = 0
    H = Graph(G)
    for i in disjointSet:
        for e in i:
            H.set_edge_label(e[0], e[1], cont)
        cont += 1

    fim = time.time()
    print('tempo de execução: ' + str(fim-inicio))
    print('Number of solves: ' + str(cont_numb_of_solves))
    return H,cont_numb_of_solves



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
        if setted[1] == 1.0:
            disjointSet.union(setted[0][0], setted[0][1])
            setted_angles.append(setted[0])
            dic[setted[0][0]].append(setted[0])
            dic[setted[0][1]].append(setted[0])
    
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


