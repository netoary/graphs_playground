"""
    TO DO
    # Revisar
    # testar funções
"""

import time
import random
from copy import deepcopy

load("utils.sage")

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


def allowCanonicalDecomposition(G, allow_k4minuses = True, allow_triangles = True, allow_squares = True, allow_connection_vertex_whithout_hanging_edge = True):
    # Canonical decomposition where it is possible to select which of the trails are formed
    # return True, if there is at least one decomposition requested
    M = G.matching(algorithm="Edmonds")
    if (len(M) != len(G) / 2):
        return False
    matchings = G.perfect_matchings()
    for M in matchings:
        graph = Graph(G)
        stop = True
        for i in M:
            graph.delete_edge(i)
        petersen = graph.two_factor_petersen()
        for i in M:
            graph.add_edge(i[0], i[1], "P")
        graph, dec = canonicalDecomposition(graph, M, petersen)
        a, b, c = badsCounter(graph)
        d = hangConnectionVertexs(graph)
        if (not allow_k4minuses and c > 0):
            stop = False
        if (not allow_triangles and a > 0):
            stop = False
        if (not allow_squares and b > 0):
            stop = False
        if (not allow_connection_vertex_whithout_hanging_edge and d):
            stop = False
        if (stop == True):
            break
    return graph, stop


def takeHangingEdges(G):
    # tests whether the decomposition is decomposing into paths
    # returns a dictionary with Hanging Edges in each vertex
    graph = Graph(G)
    hangingEdges = {}
    dic = {}
    edges = graph.edges()
    n = graph.order()
    cont = 0
    for i in range(n / 2):
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
                        dotheypointtodegree1vertex = (trail1.degree(j[0])==1 or trail1.degree(j[1])==1) and (trail2.degree(k[0]) or trail2.degree(k[1]))
                        if (not([j,k] in moves or [k,j] in moves)) and not dotheypointtodegree1vertex:
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


def full_search(G, cont=0, oldDecompositions=[]):
    # recursion that runs through the graph until it finds a path decomposition
    # returns (moves, True) if it finds, otherwise (moves, False)
    graph = Graph(G)
    hangingEdges, hangingEdgesStatus = takeHangingEdges(graph)
    if (hangingEdgesStatus == True):
        cont = cont + 1
        return cont, True

    pMoves = possibleMoves(graph, hangingEdges)
    oldDecompositions.append(graph.edges())
    for i in pMoves:
        move(graph, i)
        dec = graph.edges()
        if (dec in oldDecompositions):
            unmove(graph, i)
        else:
            cont = full_search(graph, cont, oldDecompositions)

    return cont, False


def search(graph, hangingEdges, hangingEdgesStatus, mov=[], oldDecompositions=[]):
    #recursion that runs through the graph until it finds a path decomposition
    #returns (moves, True) if it finds, otherwise (moves, False)
    if (hangingEdgesStatus == True):
        return mov, True
    pMoves = possibleMoves(graph, hangingEdges)
    var = False
    graph_aux = Graph(graph)
    oldDecompositions.append(graph_aux.edges())
    for i in pMoves:
        move(graph, i)
        dec = graph.edges()
        if (dec in oldDecompositions):
            unmove(graph, i)
        else:
            hangingEdges, hangingEdgesStatus = takeHangingEdges(graph)
            mov.append(i)
            if (hangingEdgesStatus == True):
                return mov, True
            mov, var = search(graph, hangingEdges, hangingEdgesStatus, mov, oldDecompositions)
        if (var==True):
            return mov, var
    if (var==False):
        mov = []
    return mov, var


def search_s1(graph, hangingEdges, hangingEdgesStatus, mov=[], oldDecompositions=[], max_depth=[]):
    #recursion that runs through the graph until it finds a path decomposition
    #returns (moves, True) if it finds, otherwise (moves, False)
    # Retorna em moves a profundidade da solução
    if (hangingEdgesStatus == True):
        return mov, True, max_depth
    pMoves = possibleMoves(graph, hangingEdges)
    var = False
    graph_aux = Graph(graph)
    oldDecompositions.append(graph_aux.edges())
    for i in pMoves:
        graph_aux = Graph(graph)
        move(graph_aux, i)
        dec = graph_aux.edges()
        if (dec in oldDecompositions):
            unmove(graph_aux, i)
        else:
            hangingEdges, hangingEdgesStatus = takeHangingEdges(graph_aux)
            mov.append(i)
            max_depth.append(len(mov))
            if (hangingEdgesStatus == True):
                return mov, True, max_depth
            mov, var, max_depth = search_s1(graph_aux, hangingEdges, hangingEdgesStatus, mov, oldDecompositions, max_depth)
            if (var==True):
                return mov, var, max_depth
            else:
                _ = mov.pop()
    return mov, var, max_depth


def search_s2(graph, hangingEdges, hangingEdgesStatus, mov=[], oldDecompositions=[], max_depth=[]):
    #recursion that runs through the graph until it finds a path decomposition
    #returns (moves, True) if it finds, otherwise (moves, False)
    # Retorna em moves a profundidade da solução
    if (hangingEdgesStatus == True):
        return mov, True, max_depth
    pMoves = possibleMoves(graph, hangingEdges)
    var = False
    graph_aux = Graph(graph)
    oldDecompositions.append(graph_aux.edges())
    if len(oldDecompositions) >= 100:
        return mov, var, max_depth
    for i in pMoves:
        move(graph, i)
        dec = graph.edges()
        if (dec not in oldDecompositions):
            hangingEdges, hangingEdgesStatus = takeHangingEdges(graph)
            mov.append(i)
            max_depth.append(len(mov))
            if (hangingEdgesStatus == True):
                return mov, True, max_depth
            mov, var, max_depth = search_s2(graph, hangingEdges, hangingEdgesStatus, mov, oldDecompositions, max_depth)
            if (var==True):
                return mov, var, max_depth
            else:
                _ = mov.pop()
        unmove(graph, i)
    return mov, var, max_depth


def brute_test(G, limit = 10):
    """
        Dado um Grafo G e um limite de emparelhamentos
        Retorna um dicionário com duas vezes o limite de dados contendo:
            A string g6 do grafo, o emparelhamento usado, o tempo 1, o tempo 2, 
                a profundidade da solução e se resolveu o problema
    """
    result = []
    cont_limit = 0
    for M in G.perfect_matchings():
        for i in M:
            G.delete_edge(i)
        petersen = G.two_factor_petersen()
        for i in M:
            G.add_edge(i)
        H = Graph(G)
        start_time = time.time()
        H, _ = canonicalDecomposition(H, M, petersen)
        middle_time = time.time()
        hangingEdges, hangingEdgesStatus = takeHangingEdges(H)
        moves, status, depth = search_s2(H, hangingEdges, hangingEdgesStatus, [], [], [])
        final_time = time.time()
        if depth == []:
            max_depth = 0
        else:
            max_depth = max(depth)
        result.append([G.graph6_string(), str(list(M)).replace(",","-"), middle_time - start_time, final_time - middle_time, len(moves), status, max_depth])
    
        petersen_reverse = [petersen[1], petersen[0]]
        H = Graph(G)
        start_time = time.time()
        H, _ = canonicalDecomposition(H, M, petersen_reverse)
        middle_time = time.time()
        hangingEdges, hangingEdgesStatus = takeHangingEdges(H)
        moves, status, depth = search_s2(H, hangingEdges, hangingEdgesStatus, [], [], [])
        final_time = time.time()
        if depth == []:
            max_depth = 0
        else:
            max_depth = max(depth)
        result.append([G.graph6_string(), str(list(M)).replace(",","-"), middle_time - start_time, final_time - middle_time, len(moves), status, max_depth])
        
        cont_limit += 1
        if cont_limit >= limit:
            return result
    return result
