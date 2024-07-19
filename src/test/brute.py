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
                        # file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                        file.write(str(datas)[1:-1].replace("'","").replace(" ",""))
                        file.write("\n")
                brute_dic = []
                print(n)
                logging.info(f'{n} -> {test_name}')
        with open(f'../resultados/brute_test_{test_name}.csv', 'a') as file:
            for datas in brute_dic:
                # file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                file.write(str(datas)[1:-1].replace("'","").replace(" ",""))
                file.write("\n")
        brute_dic = []
        logging.info(f'{n} -> {test_name}')
