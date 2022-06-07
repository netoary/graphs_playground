import os

load("brute_force.sage")

def test(path):
    graphs_file = open(path)
    n = 0
    for x in graphs_file:
        brute_dic = brute_test(graph, 10)