M = ((4, 7), (2, 6), (1, 5), (0, 3))

H = Graph(G)
H, _ = canonicalDecomposition(H, M, petersen)
hangingEdges, hangingEdgesStatus = takeHangingEdges(H)

H_1 = Graph(H)
hangingEdges_1 = hangingEdges
hangingEdgesStatus_1 = hangingEdgesStatus
mov_s, status_s = search(H_1, hangingEdges_1, hangingEdgesStatus_1, [], [])

H_1 = Graph(H)
hangingEdges_1 = hangingEdges
hangingEdgesStatus_1 = hangingEdgesStatus
mov_s1, status_s1, depth_s2 = search_s1(H_1, hangingEdges_1, hangingEdgesStatus_1, [], [], [])

H_1 = Graph(H)
hangingEdges_1 = hangingEdges
hangingEdgesStatus_1 = hangingEdgesStatus
mov_s2, status_s2, depth_s2 = search_s2(H_1, hangingEdges_1, hangingEdgesStatus_1, [], [], [])

# search
H_1 = Graph(H)
hangingEdges = hangingEdges_1
hangingEdgesStatus = hangingEdgesStatus_1
mov = []
oldDecompositions = []
graph = Graph(H_1)

if (hangingEdgesStatus == True):
    print(mov, True)
pMoves = possibleMoves(graph, hangingEdges)
var = False
graph_aux = Graph(graph)
oldDecompositions.append(graph_aux.edges())
for i in pMoves:
    move(graph, i)
    dec = graph.edges()
    if (dec in oldDecompositions):
        unmove(graph, i)
        print("unmove")
    else:
        hangingEdges, hangingEdgesStatus = takeHangingEdges(graph)
        mov.append(i)
        if (hangingEdgesStatus == True):
            print(mov, True)
        print("RECURSÃO")
        #mov, var = search(graph, hangingEdges, hangingEdgesStatus, mov, oldDecompositions)
    if (var==True):
        print(mov, True)
if (var==False):
    mov = []


petersen_reverse = [petersen[1], petersen[0]]

H = Graph(G)
H, _ = canonicalDecomposition(H, M, petersen_reverse)
hangingEdges, hangingEdgesStatus = takeHangingEdges(H)

H_1 = Graph(H)
hangingEdges_1 = hangingEdges
hangingEdgesStatus_1 = hangingEdgesStatus
mov_s, status_s = search(H_1, hangingEdges_1, hangingEdgesStatus_1, [], [])

H_1 = Graph(H)
hangingEdges_1 = hangingEdges
hangingEdgesStatus_1 = hangingEdgesStatus
mov_s1, status_s1, depth_s1 = search_s1(H_1, hangingEdges_1, hangingEdgesStatus_1, [], [], [])

H_1 = Graph(H)
hangingEdges_1 = hangingEdges
hangingEdgesStatus_1 = hangingEdgesStatus
mov_s2, status_s2, depth_s2 = search_s2(H_1, hangingEdges_1, hangingEdgesStatus_1, [], [], [])