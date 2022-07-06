import os
directory = './'
dic = {}
for filename in os.listdir(directory):
    path = directory+filename
    print(filename)
    #break_test = ['planar_14.g6', 'planar_16.g6', 'planar_18.g6', 'planar_20.g6', 'planar_22.g6', 'planar_24.g6', 'planar_26.g6']
    break_test = ['planar_28.g6']
    if filename in break_test:
        dic[filename] = []
        with open(filename, 'r') as graphs_file:
            for x in graphs_file:
                G = Graph(x)
                n = G.order()
                tam = G.size()
                if tam == 5/2*n:
                    dic[filename].append(x)
    


for i in dic:
    with open(f'5reg_{i}', 'a') as file:
        for data in dic[i]:
            file.write(data)
            #file.write("\n")