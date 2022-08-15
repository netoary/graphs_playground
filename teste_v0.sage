import os
import time
import logging
test_name = time.strftime("_%Y_%m_%d_%H")
logging.basicConfig(filename=f'logs/teste{test_name}.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

load("brute_force.sage")
load("direct_ILP_v2.sage")
load("direct_ILP_lazy_v3.sage")
load("angle_ILP_lazy_v1.sage")


def test_brute_froce(path, test_name, step = 10):
    with open(path, 'r') as graphs_file:
        n = 0

        with open(f'../resultados/brute_test_{test_name}.csv', 'a') as file:
            brute_dic = ['G6', 'emparelhamento', 'canonical_time', 'solve_time', 'qtde_moves', 'resultado', 'max_depth']
            file.write(str(brute_dic).replace("[","").replace("]","").replace("'","").replace(" ",""))
            file.write("\n")

        brute_dic = []

        for x in graphs_file:
            n += 1
            graph = Graph(x)
            brute_dic = brute_dic + (brute_test(graph, 10))
            if n % step == 0:
                with open(f'../resultados/brute_test_{test_name}.csv', 'a') as file:
                    for datas in brute_dic:
                        file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                        file.write("\n")
                brute_dic = []
                print(n)
                logging.info(f'{n} -> {test_name}')
        with open(f'../resultados/brute_test_{test_name}.csv', 'a') as file:
            for datas in brute_dic:
                file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                file.write("\n")
        brute_dic = []
        logging.info(f'{n} -> {test_name}')


def test_direct_ilp(path, test_name, step = 10):
    with open(path, 'r') as graphs_file:
        n = 0

        with open(f'../resultados/direct_ilp_test_{test_name}.csv', 'a') as file:
            direct_dic = ['G6', 'PLI_create_time', 'solve_time', 'resultado']
            file.write(str(direct_dic).replace("[","").replace("]","").replace("'","").replace(" ",""))
            file.write("\n")

        direct_dic = []

        for x in graphs_file:
            n += 1
            graph = Graph(x)
            direct_dic.append(direct_ILP(graph, False))
            if n % 1 == 0:
                with open(f'../resultados/direct_ilp_test_{test_name}.csv', 'a') as file:
                    for datas in direct_dic:
                        file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                        file.write("\n")
                direct_dic = []
        with open(f'../resultados/direct_ilp_test_{test_name}.csv', 'a') as file:
            for datas in direct_dic:
                file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                file.write("\n")
        direct_dic = []


def test_direct_ilp_callback(path, test_name, step = 10):
    with open(path, 'r') as graphs_file:
        n = 0

        with open(f'../resultados/direct_ilp_callback_test_{test_name}.csv', 'a') as file:
            direct_dic = ['G6', 'PLI_create_time', 'solve_time', 'result', 'counter', 'break_type']
            file.write(str(direct_dic).replace("[","").replace("]","").replace("'","").replace(" ",""))
            file.write("\n")

        direct_dic = []

        for x in graphs_file:
            n += 1
            print(x)
            graph = Graph(x)
            direct_dic.append(solve_direct_callback(graph))
            if n % step == 0:
                with open(f'../resultados/direct_ilp_callback_test_{test_name}.csv', 'a') as file:
                    for datas in direct_dic:
                        file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                        file.write("\n")
                direct_dic = []
                print(n)
                logging.info(f'{n} -> {test_name}')
        with open(f'../resultados/direct_ilp_callback_test_{test_name}.csv', 'a') as file:
            for datas in direct_dic:
                file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                file.write("\n")
        direct_dic = []
        logging.info(f'{n} -> {test_name}')


def test_angle_ilp_callback(path, test_name, step = 10):
    with open(path, 'r') as graphs_file:
        n = 0

        with open(f'../resultados/angle_ilp_callback_test_{test_name}.csv', 'a') as file:
            angle_dic = ['G6', 'PLI_create_time', 'solve_time', 'resultado']
            file.write(str(angle_dic).replace("[","").replace("]","").replace("'","").replace(" ",""))
            file.write("\n")

        angle_dic = []

        for x in graphs_file:
            n += 1
            graph = Graph(x)
            angle_dic.append(set_angle_model(graph))
            if n % step == 0:
                with open(f'../resultados/angle_ilp_callback_test_{test_name}.csv', 'a') as file:
                    for datas in angle_dic:
                        file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                        file.write("\n")
                angle_dic = []
                print(n)
                logging.info(f'{n} -> {test_name}')
        with open(f'../resultados/angle_ilp_callback_test_{test_name}.csv', 'a') as file:
            for datas in angle_dic:
                file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                file.write("\n")
        angle_dic = []
        logging.info(f'{n} -> {test_name}')


'''
test_brute_froce('graphs/5regular8-all.g6', 1, 1)
test_direct_ilp('graphs/5regular8-all.g6', 1, 1)
test_direct_ilp_callback('graphs/5regular8-all.g6', 1, 1)
test_angle_ilp_callback('graphs/5regular8-all.g6', 1, 1)
test_brute_froce('../grafos/5regular8-all.g6', 'emp_M', 1)
'''

def run_test(test_type='small', graphs=['brute'], limit=100):
    directory = '../grafos/'
    for filename in os.listdir(directory):
        path = directory+filename
        if (test_type == 'all'):
            break_test = ['5regular8-all.g6', '5regular10-all.g6', '5regular12-all.g6']
        elif (test_type == 'bipartite' or test_type == 'bipartido'):
            break_test = ['5reg_bipartite_14.g6', '5reg_bipartite_16.g6', '5reg_bipartite_18.g6', '5reg_bipartite_20.g6']
        elif (test_type == 'planar'):
            break_test = ['5reg_planar_16.g6', '5reg_planar_18.g6', '5reg_planar_20.g6', '5reg_planar_22.g6', '5reg_planar_24.g6', '5reg_planar_26.g6']
        elif (test_type == 'big'):
            break_test = ['5reg_100.g6', '5reg_1000.g6', '5reg_10000.g6']
        elif (test_type == 'small'):
            break_test = ['5regular8-all.g6']
        else:
            break_test = test_type
        if filename in break_test:
            csv_name = filename.replace(".", "_") + time.strftime("_%Y_%m_%d_%H")
            if 'brute' in graphs:
                print(f"Comecou forca bruta: {csv_name}!")
                logging.info(f'Comecou forca bruta: {filename}')
                test_brute_froce(path, csv_name, limit)
                logging.info(f'Concluiu forca bruta: {filename}')

            if 'direct' in graphs:
                print(f"Comecou ILP direto: {csv_name}!")
                logging.info(f'Comecou ILP direto: {filename}')
                test_direct_ilp_callback(path, csv_name, limit)
                logging.info(f'Concluiu ILP direto: {filename}')

            if 'angle' in graphs:
                print(f"Comecou ILP angulo: {csv_name}!")
                logging.info(f'Comecou ILP angulo: {filename}')
                test_angle_ilp_callback(path, csv_name, limit)
                logging.info(f'Concluiu ILP angulo: {filename}')


def run_direct(filename='5regular8-all.g6', limit=100):
    directory = '../grafos/'
    path = directory+filename
    csv_name = filename.replace(".", "_") + time.strftime("_%Y_%m_%d_%H")
    print(f"Comecou ILP direto: {csv_name}!")
    logging.info(f'Comecou ILP direto: {filename}')
    test_direct_ilp_callback(path, csv_name, limit)
    logging.info(f'Concluiu ILP direto: {filename}')


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
