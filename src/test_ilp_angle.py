from ilp.angle_ilp_path_decomposition_mothod import AngleILPPathDecompositionMothod
from test_abstract import TestAbstract
from sage.all import *
import os
import time
import logging



class TestAngleIlp(TestAbstract):
    def __init__(self, method) -> None:
        self.method = method
        test_name = time.strftime("_%Y_%m_%d_%H")
        logging.basicConfig(filename=f'../outputs/logs/teste{test_name}.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

    def _save_header(self, save_path):
        with open(save_path, 'a') as file:
            angle_dic = ['G6', 'PLI_create_time', 'solve_time', 'result', 'counter', 'break_type']
            file.write(str(angle_dic).replace("[","").replace("]","").replace("'","").replace(" ",""))
            file.write("\n")
        return []

    def run_test(self, path, test_name, step = 10):
        save_path = f'../outputs/angle_ilp_{test_name}.csv'
        with open(path, 'r') as graphs_file:
            n = 0

            angle_dic = self._save_header(save_path)

            for x in graphs_file:
                n += 1
                print(x)
                graph = Graph(x)
                angle = AngleILPPathDecompositionMothod(graph)
                angle_dic.append(angle.run())
                if n % step == 0:
                    angle_dic = self._save_results(save_path, angle_dic)
                    print(n)
                    logging.info(f'{n} -> {test_name}')
            angle_dic = self._save_results(save_path, angle_dic)
            logging.info(f'{n} -> {test_name}')

t = TestAngleIlp('Angle')
# t.run_planar()
# files = ['5reg_planar_18.g6', '5reg_planar_20.g6', '5reg_planar_22.g6', '5reg_planar_24.g6', '5reg_planar_26.g6']
# t.run_multiple_files(files)
# t.run_bipartite()
t.run_benchmark()
