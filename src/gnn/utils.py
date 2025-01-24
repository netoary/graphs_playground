from sage.all import *

import time
import random
from copy import deepcopy

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

def canonicalDecomposition(G, M = [], petersen = []):
    # If graph does not have perfect matching the function returns original graph, "False"
    # petersen is a list of 2-factors without M, which is a graph matching
    # For each edge in a 2-factor its label is changed
    # If for each matching of M a trail is generated (identified by the labels between 0 and (m / r) -1),
    # the function returns colored graph, "True"
    
    graph = Graph(G)
    
    if M == []:
        M = graph.matching(algorithm="Edmonds")
        
    H = Graph(graph)
    H.delete_edges(M)
    if petersen == []:
        petersen = H.two_factor_petersen()

    labeling = len(graph)
    if (len(M) != labeling/2):
        return graph, False

    cont = 0
    for i in M:
        x = i[0]
        y = i[1]
        graph.set_edge_label(x, y, cont)
        for k in range(len(petersen)):
            for j in petersen[k]:
                if (j[0] == x):
                    graph.set_edge_label(j[0], j[1], cont)
                    x = j[1]
                    break
            for j in petersen[k]:
                if (j[0] == y):
                    graph.set_edge_label(j[0], j[1], cont)
                    y = j[1]
                    break
        cont += 1
    return graph, True

def takeHangingEdges(G):
    # tests whether the decomposition is decomposing into paths
    # returns a dictionary with Hanging Edges in each vertex
    graph = Graph(G)
    hangingEdges = {}
    dic = {}
    edges = graph.edges()
    n = graph.order()
    cont = 0
    for i in range(int(n / 2)):
        dic[i] = []
    for i in edges:
        dic[i[2]].append(i)
    for i in dic:
        H = Graph(dic[i])
        for j in H.edges():
            if (mod(H.degree(j[0]), 2) == 1):
                X = Graph(H)
                X.delete_edge(j)
                if (X.is_connected() or H.degree(j[0]) == 1):
                    if (j[1] in hangingEdges):
                        hangingEdges[j[1]].append(j)
                    else:
                        hangingEdges[j[1]] = [j]
                    cont += 1

            if (mod(H.degree(j[1]), 2) == 1):
                X = Graph(H)
                X.delete_edge(j)
                if (X.is_connected() or H.degree(j[1]) == 1):
                    if (j[0] in hangingEdges):
                        hangingEdges[j[0]].append(j)
                    else:
                        hangingEdges[j[0]] = [j]
                    cont += 1
    if (cont == n):
        return [], True
    return hangingEdges, False

def takeHangingEdges_v2(G):
    # tests whether the decomposition is decomposing into paths
    # returns a dictionary with Hanging Edges in each vertex
    graph = Graph(G)
    hangingEdges = {}
    dic = {}
    edges = graph.edges()
    n = graph.order()
    cont = 0
    for i in range(int(n / 2)):
        dic[i] = []
    for i in edges:
        dic[i[2]].append(i)
    for i in dic:
        H = Graph(dic[i])
        for j in H.edges():
            if (mod(H.degree(j[0]), 2) == 1):
                X = Graph(H)
                X.delete_edge(j)
                if (X.is_connected() or H.degree(j[0]) == 1):
                    if (j[1] in hangingEdges):
                        hangingEdges[j[1]].append(j)
                    else:
                        hangingEdges[j[1]] = [j]
                    cont += 1

            if (mod(H.degree(j[1]), 2) == 1):
                X = Graph(H)
                X.delete_edge(j)
                if (X.is_connected() or H.degree(j[1]) == 1):
                    if (j[0] in hangingEdges):
                        hangingEdges[j[0]].append(j)
                    else:
                        hangingEdges[j[0]] = [j]
                    cont += 1
    if (cont == n):
        return [], True, cont
    return hangingEdges, False, cont

def definir_tipo_trilha(T):
    tamanho_trilha = len(T)
    cintura_trilha = T.girth()
    if tamanho_trilha == 4:
        return 'trilha_3'
    elif tamanho_trilha == 6:
        return 'caminho'
    elif cintura_trilha == 4:
        return 'trilha_1'
    elif cintura_trilha == 3:
        return 'trilha_2'
    else:
        return 'nao_mapeado'

def possibleMoves(graph, hangingEdges):
    #returns possible moves
    moves = []
    
    for i in hangingEdges:
        if (len(hangingEdges[i]) >= 2):
            for j in hangingEdges[i]:
                for k in hangingEdges[i]:
                    if (j[2] != k[2]):
                        trail1=Graph(extractColor(graph, j[2]))
                        trail2=Graph(extractColor(graph, k[2]))
                        # trail2.show()
                        dotheypointtodegree1vertex = (trail1.degree(j[0])==1 or trail1.degree(j[1])==1) and (trail2.degree(k[0])==1 or trail2.degree(k[1])==1)
                        if (not([j,k] in moves or [k,j] in moves)) and not dotheypointtodegree1vertex:
                            # moves.append([j, k, definir_tipo_trilha(trail1), definir_tipo_trilha(trail2)])
                            moves.append([j,k])
    return moves


def move(graph, pair):
    #change the label of the pair of edges
    graph.set_edge_label(pair[0][0], pair[0][1], pair[1][2])
    graph.set_edge_label(pair[1][0], pair[1][1], pair[0][2])


def unmove(graph, pair):
    #exchange the label of the pair of edges
    graph.set_edge_label(pair[0][0], pair[0][1], pair[0][2])
    graph.set_edge_label(pair[1][0], pair[1][1], pair[1][2])

def definir_tipo_trilha2(T):
    tamanho_trilha = len(T)
    cintura_trilha = T.girth()
    if tamanho_trilha == 4 or cintura_trilha == 4:
        return '3'
    elif tamanho_trilha == 6 and max(T.degree()) == 2:
        return '4'
    elif cintura_trilha == 4:
        return '1'
    elif cintura_trilha == 3:
        return '2'
    else:
        return '0'

def separa_cores_por_vertice(pMoves: list) -> dict:
    dic = {}
    for i in pMoves:
        if i[0][0] == i[1][0]:
            v = i[0][0]
        elif i[0][0] == i[1][1]:
            v = i[0][0]
        else:
            v = i[0][1]
        dic_v = dic.setdefault(v, [i[0][2], i[1][2]])
        if i[0][2] not in dic_v:
            dic[v].append(i[0][2])
        if i[1][2] not in dic_v:
            dic[v].append(i[1][2])
    return dic

def separa_cores_por_vertice_todo_grafo(graph) -> dict:
    dic = {}
    edges = graph.edges()
    for edge in edges:
        if i[0][0] == i[1][0]:
            v = i[0][0]
        elif i[0][0] == i[1][1]:
            v = i[0][0]
        else:
            v = i[0][1]
        dic_v = dic.setdefault(v, [i[0][2], i[1][2]])
        if i[0][2] not in dic_v:
            dic[v].append(i[0][2])
        if i[1][2] not in dic_v:
            dic[v].append(i[1][2])
    return dic

def define_estado_atual(graph, dic):
    estados = []
    for vertice, cores in dic.items():
        mapeamento_cores_para_trilhas = {}
        lista_trilhas = []
        for cor in cores:
            if cor in mapeamento_cores_para_trilhas:
                lista_trilhas.append(mapeamento_cores_para_trilhas[cor])
            else:
                T = Graph(extractColor(graph, cor))
                tipo_trilha = definir_tipo_trilha2(T)
                mapeamento_cores_para_trilhas[cor] = tipo_trilha
                lista_trilhas.append(tipo_trilha)
        lista_trilhas.sort()
        estados.append("".join(lista_trilhas))
    estados.sort()
    return estados
