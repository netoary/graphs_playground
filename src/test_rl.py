from rl.rl_path_decomposition_mothod import RLPathDecompositionMothod
from test_abstract import TestAbstract
from sage.all import *
import os
import time
import logging



class TestRL(TestAbstract):
    def __init__(self, method) -> None:
        self.method = method
        test_name = time.strftime("_%Y_%m_%d_%H")
        # logging.basicConfig(filename=f'../outputs/logs/teste{test_name}.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

    def _save_header(self, save_path):
        with open(save_path, 'a') as file:
            rl_dic = ['G6', 'emparelhamento', 'canonical_time', 'solve_time', 'qtde_moves', 'resultado', 'max_depth']
            file.write(str(rl_dic).replace("[","").replace("]","").replace("'","").replace(" ",""))
            file.write("\n")
        return []

    def _save_results(self, save_path, method_dic):
        with open(save_path, 'a') as file:
            for datas in method_dic:
                for data in datas:
                    # file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                    file.write(str(data)[1:-1].replace("'","").replace(" ",""))
                    file.write("\n")
        return []

    def run_test(self, path, test_name, step = 10):
        save_path = f'../outputs/rl_{test_name}.csv'
        with open(path, 'r') as graphs_file:
            n = 0

            rl_dic = self._save_header(save_path)

            for x in graphs_file:
                n += 1
                print(x)
                graph = Graph(x)
                rl = RLPathDecompositionMothod(graph)
                rl_dic.append(rl.run())
                if n % step == 0:
                    rl_dic = self._save_results(save_path, rl_dic)
                    print(n)
                    # logging.info(f'{n} -> {test_name}')
            rl_dic = self._save_results(save_path, rl_dic)
            # logging.info(f'{n} -> {test_name}')


t = TestRL('rl')
# t.run_planar()
t.run("5reg_planar_16.g6")
