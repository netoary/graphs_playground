import os
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import math


caminho_base = '/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/separado/'

caminho_pasta = caminho_base + 'brute'
bipartite_benchmark = {}
all_benchmark = {}
for arquivo in os.listdir(caminho_pasta):
    caminho_completo = os.path.join(caminho_pasta, arquivo)
    quebra = arquivo.split("_")
    if quebra[1] == "birpartite":
        bipartite_benchmark[quebra[1]+"_"+quebra[2]] = caminho_completo
    if quebra[1] == "all":
        all_benchmark[quebra[1]+"_"+quebra[2]] = caminho_completo

all_results = []
# testes = [bipartite_benchmark, all_benchmark]
# testes_label = ['bipartite_benchmark', 'all_benchmark']
testes = [all_benchmark, bipartite_benchmark]
testes_label = ['all_benchmark', 'bipartite_benchmark']
max_moves = 0
for total_testes in testes:
    resultados = {key: [] for key in total_testes.keys()}
    for teste, caminho in total_testes.items():
        df = pd.read_csv(caminho)

        numero_total_de_testes = len(df)
        if max_moves < max(df['qtde_moves']):
            max_moves = max(df['qtde_moves'])
        numero_solucoes = len(df.loc[df["resultado"] == True])

        razao_de_solucoes = round((numero_solucoes / numero_total_de_testes * 100), 1)

        total_de_grafos_resolvidos = len(df[["G6"]].loc[df["resultado"] == True].drop_duplicates())


        df["total_time"] = df["canonical_time"] + df["solve_time"]

        tempo_medio = df["total_time"].mean()
        desvio_do_tempo_medio = df["total_time"].std()
        
        resultados[teste].append(tempo_medio)
        resultados[teste].append(desvio_do_tempo_medio)
        resultados[teste].append(razao_de_solucoes)
        resultados[teste].append(total_de_grafos_resolvidos)
    all_results.append(resultados)


fig = plt.figure()
x = [col for col in range(10, 90, 10)]
menor_valor = np.inf
maior_valor = -np.inf
epsilon = 0.02
for idx, teste in enumerate(testes):
    y_rl = [0] * 8
    yerr_rl = [0] * 8
    for familia, valor in all_results[idx].items():
        index = int((int(familia.split("_")[-1]) / 10) -1)
        y_rl[index] = valor[0]
        menor_valor = menor_valor if menor_valor < valor[0] else valor[0]
        menor_valor = menor_valor if menor_valor < valor[1] else valor[1]
        maior_valor = maior_valor if maior_valor > valor[0] else valor[0]
        maior_valor = maior_valor if maior_valor > valor[1] else valor[1]
        yerr_rl[index] = valor[1]
    # y_rl = [math.log(col[0]) if len(col) > 0 else 0 for col in rl.values()] # TODO AJUSTAR
    # yerr_rl = [math.log(col[1]) if len(col) > 0 else 0 for col in rl.values()]
    yerr_rl = [abs(yerr) for yerr in yerr_rl]
    # plt.errorbar(x, y_rl, yerr=yerr_rl, fmt='o', label=testes_label[idx])
    plt.errorbar(x, y_rl, yerr=yerr_rl, label=testes_label[idx])

plt.xlabel("Tipo de Grafo")
# plt.ylabel("Tempo (s)")
plt.ylabel("Tempo log(s)")

plt.ylim(round(menor_valor-epsilon, 2), round(maior_valor+epsilon, 2))
plt.xticks(x)

plt.legend(loc='lower right')
plt.show()
print()