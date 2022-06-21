import os

load("brute_force.sage")

def test(path, test_name):
    graphs_file = open(path)
    n = 0

    with open(f'brute_test_{test_name}.csv', 'a') as file:
        brute_dic = ['G6', 'emparelhamento', 'tempo_meio', 'tempo_final', 'qtde_moves', 'resultado']
        for data in brute_dic:
            if data == brute_dic[-1]:
                file.writelines("% s\n" % data)
            else:
                file.writelines("% s," % data)

    brute_dic = []

    for x in graphs_file: # ['GFzvvW']:
        n += 1
        graph = Graph(x)
        brute_dic = brute_dic + (brute_test(graph, 10))
        print(brute_dic)
        if n % 1 == 0:
            with open(f'brute_test_{test_name}.csv', 'a') as file:
                # file.writelines("\n")
                # file.writelines("% s," % data if data != datas[-1] else "% s\n" for datas in brute_dic for data in datas)
                for datas in brute_dic:
                    for data in datas:
                        if data == datas[-1]:
                            file.writelines("% s\n" % data)
                        else:
                            file.writelines("% s," % data)

test('graphs/5regular8-all.g6', 1)

'''
directory = '../../graphs/'
for filename in os.listdir(directory):
    path = directory+filename
'''
