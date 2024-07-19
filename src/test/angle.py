from src.ilp.angle_ilp_path_decomposition_mothod import AngleILPPathDecompositionMothod
from sage.all import *
import os
import time
import logging


class TestAngleIlp():
    def __init__(self) -> None:
        test_name = time.strftime("_%Y_%m_%d_%H")
        logging.basicConfig(filename=f'../../outputs/logs/teste{test_name}.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

    def _save_header(self, save_path):
        with open(save_path, 'a') as file:
            angle_dic = ['G6', 'PLI_create_time', 'solve_time', 'result', 'counter', 'break_type']
            file.write(str(angle_dic).replace("[","").replace("]","").replace("'","").replace(" ",""))
            file.write("\n")
        return []

    def _save_results(self, save_path, angle_dic):
        with open(save_path, 'a') as file:
            for datas in angle_dic:
                # file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                file.write(str(datas)[1:-1].replace("'","").replace(" ",""))
                file.write("\n")
        return []

    def run_test_angle_ilp(self, path, test_name, step = 10):
        save_path = f'../../outputs/angle_ilp_{test_name}.csv'
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
    
    def run(self, filename: str, limit: int = 100):
        directory = '../../graphs/'
        path = directory + filename
        csv_name = filename.replace(".", "_") + time.strftime("_%Y_%m_%d_%H")
        print(f"Comecou ILP angle: {csv_name}!")
        logging.info(f'Comecou ILP direto: {filename}')
        self.run_test_angle_ilp(path, csv_name, limit)
        logging.info(f'Concluiu ILP angle: {filename}')

    def run_multiple_files(self, files: list, limit: int = 100):
        for file in files:
            self.run(file, limit)

    def run_small(self, limit: int = 100):
        self.run('5regular8-all.g6', limit)

    def run_planar(self, limit: int = 100):
        files = ['5reg_planar_16.g6', '5reg_planar_18.g6', '5reg_planar_20.g6', '5reg_planar_22.g6', '5reg_planar_24.g6', '5reg_planar_26.g6']
        self.run_multiple_files(files, limit)

    def run_bipartite(self, limit: int = 100):
        files = ['5reg_bipartite_14.g6', '5reg_bipartite_16.g6', '5reg_bipartite_18.g6', '5reg_bipartite_20.g6']
        self.run_multiple_files(files, limit)

    def run_big(self, limit: int = 100):
        files = ['5reg_100.g6', '5reg_1000.g6', '5reg_10000.g6']
        self.run_multiple_files(files, limit)

    def run_all(self, limit: int = 100):
        files = ['5regular8-all.g6', '5regular10-all.g6', '5regular12-all.g6']
        self.run_multiple_files(files, limit)

t = TestAngleIlp()
t.run_small()