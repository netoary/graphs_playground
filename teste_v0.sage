import os

load("brute_force.sage")
load("direct_ILP_v2.sage")
load("direct_ILP_lazy_v3.sage")
load("angle_ILP_lazy_v1.sage")


def test_brute_froce(path, test_name, step = 10):
    with open(path, 'r') as graphs_file:
        n = 0

        with open(f'tests/brute_test_{test_name}.csv', 'a') as file:
            brute_dic = ['G6', 'emparelhamento', 'tempo_meio', 'tempo_final', 'qtde_moves', 'resultado']
            file.write(str(brute_dic).replace("[","").replace("]",""))
            file.write("\n")

        brute_dic = []

        for x in graphs_file:
            n += 1
            graph = Graph(x)
            brute_dic = brute_dic + (brute_test(graph, 10))
            if n % 1 == 0:
                with open(f'tests/brute_test_{test_name}.csv', 'a') as file:
                    for datas in brute_dic:
                        file.write(str(datas).replace("[","").replace("]",""))
                        file.write("\n")
                brute_dic = []
        with open(f'tests/brute_test_{test_name}.csv', 'a') as file:
            for datas in brute_dic:
                file.write(str(datas).replace("[","").replace("]",""))
                file.write("\n")
        brute_dic = []


def test_direct_ilp(path, test_name, step = 10):
    with open(path, 'r') as graphs_file:
        n = 0

        with open(f'tests/direct_ilp_test_{test_name}.csv', 'a') as file:
            direct_dic = ['G6', 'tempo_meio', 'tempo_final', 'resultado']
            file.write(str(direct_dic).replace("[","").replace("]",""))
            file.write("\n")

        direct_dic = []

        for x in graphs_file:
            n += 1
            graph = Graph(x)
            direct_dic.append(direct_ILP(graph, False))
            if n % 1 == 0:
                with open(f'tests/direct_ilp_test_{test_name}.csv', 'a') as file:
                    for datas in direct_dic:
                        file.write(str(datas).replace("[","").replace("]",""))
                        file.write("\n")
                direct_dic = []
        with open(f'tests/direct_ilp_test_{test_name}.csv', 'a') as file:
            for datas in direct_dic:
                file.write(str(datas).replace("[","").replace("]",""))
                file.write("\n")
        direct_dic = []


def test_direct_ilp_callback(path, test_name, step = 10):
    with open(path, 'r') as graphs_file:
        n = 0

        with open(f'tests/direct_ilp_callback_test_{test_name}.csv', 'a') as file:
            direct_dic = ['G6', 'tempo_meio', 'tempo_final', 'resultado']
            file.write(str(direct_dic).replace("[","").replace("]",""))
            file.write("\n")

        direct_dic = []

        for x in graphs_file:
            n += 1
            graph = Graph(x)
            direct_dic.append(solve_direct_callback(graph))
            if n % 1 == 0:
                with open(f'tests/direct_ilp_callback_test_{test_name}.csv', 'a') as file:
                    for datas in direct_dic:
                        file.write(str(datas).replace("[","").replace("]",""))
                        file.write("\n")
                direct_dic = []
        with open(f'tests/direct_ilp_callback_test_{test_name}.csv', 'a') as file:
            for datas in direct_dic:
                file.write(str(datas).replace("[","").replace("]",""))
                file.write("\n")
        direct_dic = []


def test_angle_ilp_callback(path, test_name, step = 10):
    with open(path, 'r') as graphs_file:
        n = 0

        with open(f'tests/angle_ilp_callback_test_{test_name}.csv', 'a') as file:
            angle_dic = ['G6', 'tempo_meio', 'tempo_final', 'resultado']
            file.write(str(angle_dic).replace("[","").replace("]",""))
            file.write("\n")

        angle_dic = []

        for x in graphs_file:
            n += 1
            graph = Graph(x)
            angle_dic.append(set_angle_model(graph))
            if n % step == 0:
                with open(f'tests/angle_ilp_callback_test_{test_name}.csv', 'a') as file:
                    for datas in angle_dic:
                        file.write(str(datas).replace("[","").replace("]",""))
                        file.write("\n")
                angle_dic = []
        with open(f'tests/angle_ilp_callback_test_{test_name}.csv', 'a') as file:
            for datas in angle_dic:
                file.write(str(datas).replace("[","").replace("]",""))
                file.write("\n")
        angle_dic = []


'''
test_brute_froce('graphs/5regular8-all.g6', 1, 1)
test_direct_ilp('graphs/5regular8-all.g6', 1, 1)
test_direct_ilp_callback('graphs/5regular8-all.g6', 1, 1)
test_angle_ilp_callback('graphs/5regular8-all.g6', 1, 1)
'''

'''
directory = 'graphs/'
for filename in os.listdir(directory):
    path = directory+filename
'''
