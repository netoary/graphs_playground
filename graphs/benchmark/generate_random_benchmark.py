from sage.all import *


# G.is_bipartite() and G.is_planar() and G.is_regular(3)
# G = graphs.RandomBicubicPlanar(n)
# g = graphs.RandomBipartite(5, 2, 0.5)



# G = graphs.RandomRegular(3, 8)  
# g = graphs.RandomRegularBipartite(4, 6, 3)

def generate_random_g6_list_regular_graphs(d: int, n: int, list_lengh: int) -> list:
    return [graphs.RandomRegular(d, n).graph6_string() for i in range(list_lengh)]


def generate_random_g6_list_regular_birpartite_graphs(n1: int, n2: int, d: int, list_lengh: int) -> list:
    return [graphs.RandomRegularBipartite(n1, n2, d).graph6_string() for i in range(list_lengh)]


# no_filter_benchmark = [generate_random_g6_list_regular_graphs(5, (i+1)*10, 10) for i in range(10)]
multiplicador = 100
numero_de_grafos = 10
for i in range(numero_de_grafos):
    f = open(f"graphs_playground/graphs/benchmark/extra_big/all_{(i+1)*multiplicador}.g6", "w")
    graphs_sample = generate_random_g6_list_regular_graphs(5, (i+1)*multiplicador, numero_de_grafos)
    for graph in graphs_sample:
        f.write(graph)
        f.write("\n")
    f.close()


# bipartite_benchmark = [generate_random_g6_list_regular_birpartite_graphs(int((i+1)*10/2), int((i+1)*10/2), 5, 10) for i in range(10)]
for i in range(numero_de_grafos):
    f = open(f"graphs_playground/graphs/benchmark/extra_big/birpartite_{(i+1)*multiplicador}.g6", "w")
    graphs_sample = generate_random_g6_list_regular_birpartite_graphs(int((i+1)*multiplicador/2), int((i+1)*multiplicador/2), 5, numero_de_grafos)
    for graph in graphs_sample:
        f.write(graph)
        f.write("\n")
    f.close()


print('foi')