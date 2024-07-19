from sage.all import *
import os
import time
import logging


class TestAbstract():
    def __init__(self, method) -> None:
        self.method = method
        test_name = time.strftime("_%Y_%m_%d_%H")
        logging.basicConfig(filename=f'../outputs/logs/teste{test_name}.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

    def _save_results(self, save_path, method_dic):
        with open(save_path, 'a') as file:
            for datas in method_dic:
                # file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                file.write(str(datas)[1:-1].replace("'","").replace(" ",""))
                file.write("\n")
        return []

    def run_test(self, path, test_name, step = 10):
        pass

    def run(self, filename: str, limit: int = 100):
        directory = '../graphs/'
        path = directory + filename
        csv_name = filename.split('/')[-1].replace(".", "_") + time.strftime("_%Y_%m_%d_%H")
        print(f"Comecou {self.method}: {csv_name}!")
        logging.info(f'Comecou {self.method}: {filename}')
        self.run_test(path, csv_name, limit)
        logging.info(f'Concluiu {self.method}: {filename}')

    def run_multiple_files(self, files: list, limit: int = 100):
        for file in files:
            self.run(file, limit)

    def run_small(self, limit: int = 100):
        self.run('5regular8-all.g6', limit)

    def run_planar(self, limit: int = 100):
        files = ['5reg_planar_16.g6', '5reg_planar_18.g6', '5reg_planar_20.g6', '5reg_planar_22.g6', '5reg_planar_24.g6', '5reg_planar_26.g6']
        self.run_multiple_files(files, limit)

    def run_bipartite(self, limit: int = 100):
        # files = ['5reg_bipartite_14.g6', '5reg_bipartite_16.g6', '5reg_bipartite_18.g6', '5reg_bipartite_20.g6']
        files = ['5reg_bipartite_14.g6', '5reg_bipartite_16.g6', '5reg_bipartite_18.g6']
        self.run_multiple_files(files, limit)

    def run_big(self, limit: int = 100):
        files = ['5reg_100.g6', '5reg_1000.g6', '5reg_10000.g6']
        self.run_multiple_files(files, limit)

    def run_all(self, limit: int = 100):
        files = ['5regular8-all.g6', '5regular10-all.g6', '5regular12-all.g6']
        self.run_multiple_files(files, limit)

    def run_benchmark(self, limit: int = 100):
        files_all = [f"benchmark/all_{(i+1)*10}.g6" for i in range(8)]
        files_birpartite = [f"benchmark/birpartite_{(i+1)*10}.g6" for i in range(8)]
        files = files_all + files_birpartite
        self.run_multiple_files(files, limit)

    def run_benchmark_birpartite(self, limit: int = 100):
        files = [f"benchmark/birpartite_{(i+1)*10}.g6" for i in range(8)]
        self.run_multiple_files(files, limit)
