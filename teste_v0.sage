import os

load("brute_force.sage")
load("direct_ILP_v2.sage")
load("direct_ILP_lazy_v3.sage")
load("angle_ILP_lazy_v1.sage")


def test_brute_froce(path, test_name, step = 10):
    with open(path, 'r') as graphs_file:
        n = 0

        with open(f'tests/brute_test_{test_name}.csv', 'a') as file:
            brute_dic = ['G6', 'emparelhamento', 'canonical_time', 'solve_time', 'qtde_moves', 'resultado']
            file.write(str(brute_dic).replace("[","").replace("]",""))
            file.write("\n")

        brute_dic = []

        for x in graphs_file:
            n += 1
            graph = Graph(x)
            brute_dic = brute_dic + (brute_test(graph, 10))
            if n % step == 0:
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
            direct_dic = ['G6', 'PLI_create_time', 'solve_time', 'resultado']
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
            direct_dic = ['G6', 'PLI_create_time', 'solve_time', 'resultado']
            file.write(str(direct_dic).replace("[","").replace("]",""))
            file.write("\n")

        direct_dic = []

        for x in graphs_file:
            n += 1
            graph = Graph(x)
            direct_dic.append(solve_direct_callback(graph))
            if n % step == 0:
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
            angle_dic = ['G6', 'PLI_create_time', 'solve_time', 'resultado']
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



directory = '../grafos/'
for filename in os.listdir(directory):
    path = directory+filename
    break_test = ['5regular14-all', 'regular-sample.g6', 'sample18.g6', 'sample24.g6']
    # break_test.append('5regular12-all.g6')
    if filename not in break_test:
        test_direct_ilp_callback(path, filename, 10)
        test_angle_ilp_callback(path, filename, 10)
        print(path)


'''
def test_direct_ilp2(path, test_name, step = 10):
    with open(path, 'r') as graphs_file:
        n = 0

        with open(f'direct_ilp_test_{test_name}.csv', 'a') as file:
            direct_dic = ['G6', 'PLI_create_time', 'solve_time', 'resultado']
            file.write(str(direct_dic).replace("[","").replace("]",""))
            file.write("\n")

        direct_dic = []

        for x in graphs_file:
            n += 1
            graph = Graph(x)
            direct_dic.append(direct_ILP(graph, False))
            if n % step == 0:
                with open(f'direct_ilp_test_{test_name}.csv', 'a') as file:
                    for datas in direct_dic:
                        file.write(str(datas).replace("[","").replace("]",""))
                        file.write("\n")
                direct_dic = []
        with open(f'direct_ilp_test_{test_name}.csv', 'a') as file:
            for datas in direct_dic:
                file.write(str(datas).replace("[","").replace("]",""))
                file.write("\n")
        direct_dic = []

#test_direct_ilp2('graphs/5regular8-all.g6', 2, 1)
'''
