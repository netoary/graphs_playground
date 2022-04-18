"""
    TO DO
    # testar funções
"""


def dictionaryMaker(edges, n):
    # returns a dictionary containing the edges separated by the label (from 0 to n / 2)
    # edges=graph.edges()
    # n = graph.order()
    color_dic = {}
    for i in range(n/2):
        color_dic[i]=[]
    for i in edges:
        color_dic[i[2]].append(i)
    return color_dic


"""
extractColor(G,c) --> 
edges = G.edges()
[e for e in edges if e[2] == c]
"""


def extractColor(graph, color):
    # returns a list of the edges that have this color.
    edges = graph.edges()
    return [e for e in edges if e[2] == color]


def isTrail(subgraph):
    # Checks whether a subgraph is an open trail
    # returns True if it is and otherwise False
    if (subgraph.is_connected()):
        aux = 0
        for i in subgraph.degree():
            if (mod(i,2)==1):
                aux +=1
        if (aux == 2):
            return True
    return False


def isTrailDecomposition(graph):
    # tests whether the decomposition is decomposing into paths
    # returns True if it is and otherwise False
    edges = graph.edges()
    n = graph.order()
    dic = dictionaryMaker(edges, n)
    for i in dic:
        H = Graph(dic[i])
        if (isTrail(H) == False):
            return False
    return True


def is_d_Decomposition(graph):
    # test whether a given labeling is a d-decomposition
    # i.e. if the frequency of each edge label is the same
    # returns True if it is and otherwise False
    aux = 0
    n = graph.order()
    labels = []
    d = []
    for e in graph.edges():
        labels.append(graph.edge_label(e[0], e[1]))
    for label in labels:
        d.append(labels.count(label))
    cont = d.count(d[0])
    for i in d:
        if (d.count(i) != cont):
            return False
    return True


def labelInducesTrail(graph):
    # tests whether a given labeling induces a decomposition into trails
    # returns True if all colors induce 
    if(is_d_Decomposition(graph) == False):
        return False
    edges = graph.edges()
    n = graph.order()
    dic = dictionaryMaker(edges, n)
    for i in dic:
        H = Graph(dic[i])
        if (isTrail(H) == False):
            return False
    return True


def isPath(graph):
    # return True whether an element is a path
    if (isTrail(graph) == False):
        return False
    l = graph.degree()
    if (max(l) == 2):
        return True
    return False


def isPathDecomposition(graph):
    # return True whether the decomposition is decomposing into paths
    edges = graph.edges()
    n = graph.order()
    dic = dictionaryMaker(edges, n)
    for i in dic:
        H = Graph(dic[i])
        if (isPath(H) == False):
            return False
    return True