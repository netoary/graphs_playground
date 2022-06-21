import time

#Uma função que retorna todos os caminhos de comprimento 5 de G
def five_paths(G):
    paths=[]
    for e in G.edges():
        u,v,_ = e
        for x1 in G.neighbors(u):
            if x1 != v:
                for x2 in G.neighbors(x1):
                    if x2 not in [u, v]:
                        for x3 in G.neighbors(v):
                            if x3 not in [x2, x1, u]:
                                for x4 in G.neighbors(x3):
                                    if x4 not in [x2, x1, u, v]:
                                        paths.append([x2, x1, u, v, x3, x4])
    return paths

def pair_to_edge(u, v):
    if v > u:
        return (u, v)
    else:
        return (v, u)
    
def vertex_path_to_edge_path(vertex_path):
    result = []
    for i in range(5):
        x = vertex_path[i]
        y = vertex_path[i+1]
        result.append(pair_to_edge(x, y))
    return result

def paths_to_dic_edges(G, paths):
    dic = {}
    for e in G.edges(labels=False):
          dic[e] = []
    for path in paths:
        edge_path = vertex_path_to_edge_path(path)
        for e in edge_path:
            dic[e].append(path)
    return dic
            
def direct_ILP(G, colored_graph = False):
    start_time = time.time()
    p = MixedIntegerLinearProgram(maximization=False, solver="GUROBI")
    w = p.new_variable(binary=True)
    x = p.new_variable(binary=True)
    objective = 0
    paths = five_paths(G)
    dic = paths_to_dic_edges(G,paths)

    for edge in dic:
        u,v=edge
        objective+=x[u,v]
        edge_constraint=x[edge]
        for path in dic[edge]:
            a,b,c,d,e,f=path
            edge_constraint+=w[a,b,c,d,e,f]
        p.add_constraint(edge_constraint==1)
    p.set_objective(objective)

    middle_time = time.time()
    p.solve()
    final_time = time.time()
    colored_edges = 0
    # como vou saber que não temos solução?
    status = True
    if (colored_graph):
        sol = p.get_values(w).items()
        setted = []
        for x in sol:
            if x[1] == 1.0:
                print(x[0])
                setted.append(x[0])
                colored_edges += 5
        cor = 0
        for x in setted:
            for e in vertex_path_to_edge_path(x):
                G.set_edge_label(e[0], e[1], cor)
            cor+=1
    return [G.graph6_string(), middle_time - start_time, final_time - middle_time, status]


"""
G = graphs.RandomRegular(5, 20)
print(direct_ILP(G))
G.show(color_by_label=True, layout="circular")
"""