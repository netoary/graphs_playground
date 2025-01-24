import os
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import math


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Criando um DataFrame de exemplo
data = pd.DataFrame({
    'Categoria': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Distribuição 1': [5, 6, 7, 4, 5, 6, 8, 9, 10],
    'Distribuição 2': [3, 4, 5, 2, 3, 4, 7, 6, 8]
})

# Transformar os dados para o formato 'long'
data_long = pd.melt(data, id_vars=['Categoria'], var_name='Distribuição', value_name='Valor')

# # Criar o boxplot com comparação
# sns.boxplot(x='Categoria', y='Valor', hue='Distribuição', data=data_long)

# # Adicionar título
# plt.title('Comparação de Distribuições por Categoria')

# # Exibir o gráfico
# plt.show()

caminho_pasta = '/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/big/'

rl_bipartite_benchmark = {}
rl_all_benchmark = {}
brute_bipartite_benchmark = {}
brute_all_benchmark = {}
gnn_bipartite_benchmark = {}
gnn_all_benchmark = {}
for arquivo in os.listdir(caminho_pasta):
    caminho_completo = os.path.join(caminho_pasta, arquivo)
    quebra = arquivo.split("_")
    if quebra[1] == "birpartite" and quebra[0] == 'rl':
        rl_bipartite_benchmark[quebra[1]+"_"+quebra[2]] = caminho_completo
    if quebra[1] == "all" and quebra[0] == 'rl':
        rl_all_benchmark[quebra[1]+"_"+quebra[2]] = caminho_completo
    if quebra[1] == "birpartite" and quebra[0] == 'brute':
        brute_bipartite_benchmark[quebra[1]+"_"+quebra[2]] = caminho_completo
    if quebra[1] == "all" and quebra[0] == 'brute':
        brute_all_benchmark[quebra[1]+"_"+quebra[2]] = caminho_completo
    if quebra[1] == "birpartite" and quebra[0] == 'gnn':
        gnn_bipartite_benchmark[quebra[1]+"_"+quebra[2]] = caminho_completo
    if quebra[1] == "all" and quebra[0] == 'gnn':
        gnn_all_benchmark[quebra[1]+"_"+quebra[2]] = caminho_completo

all_results = []
# testes = [rl_bipartite_benchmark, rl_all_benchmark, brute_bipartite_benchmark, brute_all_benchmark, gnn_bipartite_benchmark, gnn_all_benchmark]
# testes_label = ['rl_bipartite_benchmark', 'rl_all_benchmark', 'brute_bipartite_benchmark', 'brute_all_benchmark', 'gnn_bipartite_benchmark', 'gnn_all_benchmark']

# testes = [rl_bipartite_benchmark, rl_all_benchmark, brute_bipartite_benchmark, brute_all_benchmark]
# testes_label = ['RL grafos bipartidos', 'RL todos os grafos', 'Algorito 1 grafos bipartidos', 'Algorito 1 todos os grafos']


testes = [rl_all_benchmark, brute_all_benchmark, rl_bipartite_benchmark, brute_bipartite_benchmark]
testes_label = ['RL todos os grafos', 'Algoritmo de Busca todos os grafos', 'RL grafos bipartidos', 'Algoritmo de Busca grafos bipartidos']

all_results_total_moves = []
all_results_razao_de_solucoes = []
for total_testes in testes:
    resultados_total_moves = 0
    resultados_razao_de_solucoes = 0
    for teste, caminho in total_testes.items():
        df = pd.read_csv(caminho)

        numero_total_de_testes = len(df)
        numero_solucoes = len(df.loc[df["resultado"] == True])

        razao_de_solucoes = round((numero_solucoes / numero_total_de_testes * 100), 1)

        total_moves = df['qtde_moves'].sum()
        
        resultados_total_moves += total_moves
        resultados_razao_de_solucoes += razao_de_solucoes
    all_results_total_moves.append(resultados_total_moves)
    all_results_razao_de_solucoes.append(resultados_razao_de_solucoes)

for total_testes in testes:
    resultados = {key: [] for key in total_testes.keys()}
    for teste, caminho in total_testes.items():
        df = pd.read_csv(caminho)

        numero_total_de_testes = len(df)
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

'''

fig = plt.figure()
x = [col for col in range(100, 1100, 100)]
cores = ['blue', 'orange', 'green', 'red']
for idx, teste in enumerate(testes):
    y_rl = [0] * 10
    yerr_rl = [0] * 10
    for familia, valor in all_results[idx].items():
        index = int((int(familia.split("_")[-1]) / 100) -1)
        y_rl[index] = valor[0]
        yerr_rl[index] = valor[1]
    # y_rl = [math.log(col[0]) if len(col) > 0 else 0 for col in rl.values()] # TODO AJUSTAR
    # yerr_rl = [math.log(col[1]) if len(col) > 0 else 0 for col in rl.values()]
    yerr_rl = [abs(yerr) for yerr in yerr_rl]
    # plt.errorbar(x, y_rl, yerr=yerr_rl, label=testes_label[idx], color='blue')
    plt.errorbar(x, y_rl, label=testes_label[idx], color=cores[idx])

plt.xlabel("Número de vértices")
# plt.ylabel("Tempo (s)")
plt.ylabel("Tempo (s)")

plt.legend(loc='upper left')
plt.grid(True, color='lightgray', linestyle='-', linewidth=0.7)
plt.savefig('line_graph_extra_large.png', format='png', dpi=300, bbox_inches='tight')

plt.show()

print()

'''



box_plot_bipartido = {
    'Número de vértices': sum([[i]*20 for i in range(100, 1100, 100)], []),
    'RL': [],
    'Brute': []
}

testes_bipartido = [rl_bipartite_benchmark, brute_bipartite_benchmark]
m = 0
for total_testes in testes_bipartido:
    auxiliar = {}
    metodo = "RL" if m == 0 else "Brute"
    for teste, caminho in total_testes.items():
        categoria = teste.split("_")[-1]
        df = pd.read_csv(caminho)
        df = df.loc[df['resultado'] == True]
        df[metodo] = df["canonical_time"] + df["solve_time"]
        df[metodo] = df["solve_time"]
        # df[metodo] = df["qtde_moves"]

        df = df[[metodo]]
        df = df.to_dict("list")

        auxiliar[categoria] = df[metodo]
    for i in range(100, 1100, 100):
        box_plot_bipartido[metodo].append(auxiliar[str(i)])

    m = 1

box_plot_bipartido['RL'] = sum(box_plot_bipartido['RL'], [])
box_plot_bipartido['Algoritmo de Busca'] = sum(box_plot_bipartido['Brute'], [])

del box_plot_bipartido['Brute']
data = pd.DataFrame(box_plot_bipartido)

data_long = pd.melt(data, id_vars=['Número de vértices'], var_name='Método', value_name='Tempo (s)')

'''
ax = sns.boxplot(x='Número de vértices', y='Tempo (s)', hue='Método', data=data_long)
ax.set_axisbelow(True) 
# plt.title('Comparação de distribuições por tamanho de grafo bipartido', fontsize=10)
# plt.ylim(0, 1.8)
# plt.yticks(np.arange(0, 2, 0.2)) 
plt.grid(True, color='lightgray', linestyle='-', linewidth=0.7)

colors = ["green", "red"]
i = 0
# for patch, color in zip(ax.patches, colors*11):
for patch in ax.patches:
    if i == 1:
        patch.set_facecolor("green")
    else:
        patch.set_facecolor(colors[i % 2])
    i += 1
# Adiciona uma legenda personalizada
custom_legend = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(custom_legend, ["RL", "Algoritmo de Busca"], title="Método")

plt.savefig('boxplot_extra_large_bipartite.png', format='png', dpi=300, bbox_inches='tight')

plt.show()
'''


box_plot_all = {
    'Número de vértices': sum([[i]*20 for i in range(100, 1100, 100)], []),
    'RL': [],
    'Brute': []
}
testes_all = [rl_all_benchmark, brute_all_benchmark]
m = 0
for total_testes in testes_all:
    auxiliar = {}
    metodo = "RL" if m == 0 else "Brute"
    for teste, caminho in total_testes.items():
        categoria = teste.split("_")[-1]
        df = pd.read_csv(caminho)
        df = df.loc[df['resultado'] == True]
        df[metodo] = df["canonical_time"] + df["solve_time"]
        df[metodo] = df["solve_time"]
        # df[metodo] = df["qtde_moves"]

        df = df[[metodo]]
        df = df.to_dict("list")

        auxiliar[categoria] = df[metodo]
    for i in range(100, 1100, 100):
        box_plot_all[metodo].append(auxiliar[str(i)])

    m = 1

box_plot_all['RL'] = sum(box_plot_all['RL'], [])
box_plot_all['Algoritmo de Busca'] = sum(box_plot_all['Brute'], [])

del box_plot_all['Brute']

data = pd.DataFrame(box_plot_all)

data_long = pd.melt(data, id_vars=['Número de vértices'], var_name='Método', value_name='Tempo (s)')

ax = sns.boxplot(x='Número de vértices', y='Tempo (s)', hue='Método', data=data_long)
ax.set_axisbelow(True) 
# plt.title('Comparação de distribuições por tamanho de grafo', fontsize=12)
# plt.ylim(0, 1.8)
# plt.yticks(np.arange(0, 2, 0.2)) 
plt.grid(True, color='lightgray', linestyle='-', linewidth=0.7)
plt.savefig('boxplot_extra_large_all.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
print()

#'''