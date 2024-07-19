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
                        # file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                        file.write(str(datas)[1:-1].replace("'","").replace(" ",""))
                        file.write("\n")
                direct_dic = []
                print(n)
                logging.info(f'{n} -> {test_name}')
        with open(f'../resultados/direct_ilp_callback_test_{test_name}.csv', 'a') as file:
            for datas in direct_dic:
                # file.write(str(datas).replace("[","").replace("]","").replace("'","").replace(" ",""))
                file.write(str(datas)[1:-1].replace("'","").replace(" ",""))
                file.write("\n")
        direct_dic = []
        logging.info(f'{n} -> {test_name}')