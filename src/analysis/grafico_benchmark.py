import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math




caminho_base = '/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/benchmark/'

# metodos = ["rl", "brute", "direct", "angle"]

# metodos = ["rl", "brute", "direct"]

metodos = ["rl", "brute"]

testes = {}

for metodo in metodos:
    caminho_pasta = caminho_base + metodo
    testes[metodo] = {}
    testes[metodo]["birpartite"] = {}
    testes[metodo]["all"] = {}

    for arquivo in os.listdir(caminho_pasta):
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        quebra = arquivo.split("_")
        if quebra[1] == "birpartite":
            testes[metodo]["birpartite"][quebra[2]] = caminho_completo
        if quebra[2] == "birpartite":
            testes[metodo]["birpartite"][quebra[3]] = caminho_completo
        if quebra[1] == "all":
            testes[metodo]["all"][quebra[2]] = caminho_completo
        if quebra[2] == "all":
            testes[metodo]["all"][quebra[3]] = caminho_completo



all_results = {}
testes_label = ['rl_bipartite_benchmark_12', 'rl_bipartite_benchmark_04', 'rl_all_benchmark']
for metodo, teste_metodo in testes.items():
    # resultados = {key: [] for key in metodo.keys()}
    resultados_metodo = {}

    for tipo_grafo, teste_grafo in teste_metodo.items():
        resultados_tipo_grafo = {}
        for tamanho_grafico, caminho in teste_grafo.items():
            df = pd.read_csv(caminho)
            if metodo in ["brute", "rl"]:
                df["total_time"] = df["canonical_time"] + df["solve_time"]
                df = df.loc[df['resultado'] == True]
            else:
                df["total_time"] = df["PLI_create_time"] + df["solve_time"]
                df = df.loc[df['result'] == True]

            tempo_medio = df["total_time"].mean()
            desvio_do_tempo_medio = df["total_time"].std()
            resultados_tipo_grafo[tamanho_grafico] = [tempo_medio, desvio_do_tempo_medio]
        resultados_metodo[tipo_grafo] = resultados_tipo_grafo
    all_results[metodo] = resultados_metodo


### GRAFICO DE LINHA

x = [col for col in range(10, 90, 10)]

y_all = {}
yerr_all = {}

y_bipartite = {}
yerr_bipartite = {}
for metodo, d in all_results.items():
    for tipo_grafo, dd in d.items():
        y = [0] * 8
        yerr = [0] * 8
        for idx, value in enumerate(x):
            y[idx] = dd.get(str(value), [0])[0]
            yerr[idx] = dd.get(str(value), [0,0])[1]
        yerr = [abs(yer) for yer in yerr]
        if tipo_grafo == 'all':
            y_all[metodo] = y
            yerr_all[metodo] = yerr
        else:
            y_bipartite[metodo] = y
            yerr_bipartite[metodo] = yerr

# TODO: ajustar gráfico
# testar log



fig = plt.figure()
# for metodo, y in y_all.items():
#     plt.errorbar(x, y, yerr=yerr_all[metodo], label=metodo)


plt.errorbar(x, y_all['rl'], label='RL todos os grafos', color='blue')
plt.errorbar(x, y_all['brute'], label='Algoritmo de Busca todos os grafos', color='orange')
# plt.errorbar(x, y_all['direct'], yerr=yerr_all['direct'], label='direct')
# plt.errorbar(x, y_all['angle'], yerr=yerr_all['angle'], label='angle')

plt.errorbar(x, y_bipartite['rl'], label='RL grafos bipartidos', color='green')
plt.errorbar(x, y_bipartite['brute'], label='Algoritmo de Busca grafos bipartidos', color='red')

plt.xlabel("Número de vértices")
plt.ylabel("Tempo (s)")
# plt.ylabel("Tempo log(s)")

plt.legend(loc='upper left')
# Ajustando o layout para evitar sobreposição
plt.tight_layout()
plt.grid(True, color='lightgray', linestyle='-', linewidth=0.7)

plt.savefig('line_graph_benchmark.png', format='png', dpi=300, bbox_inches='tight')

plt.show()

print()



# fig = plt.figure()
# for metodo, y in y_bipartite.items():
#     plt.errorbar(x, y, yerr=yerr_bipartite[metodo], label=metodo)

# plt.xlabel("Tipo de Grafo")
# # plt.ylabel("Tempo (s)")
# plt.ylabel("Tempo log(s)")

# plt.legend(loc='lower right')
# plt.show()
# print()



box_plot_all = {
    'Número de vértices': sum([[i]*10 for i in range(10, 90, 10)], []),
    # 'Número de vértices': [10] + sum([[i]*10 for i in range(20, 80, 10)], []),
    'rl': [],
    'brute': [],
    # 'direct': []
}

for metodo, teste_metodo in testes.items():
    auxiliar = {}
    for tipo_grafo, teste_grafo in teste_metodo.items():
        # if tipo_grafo == 'birpartite':
        if tipo_grafo == 'all':
            for tamanho_grafico, caminho in teste_grafo.items():
                df = pd.read_csv(caminho)

                df_time = pd.DataFrame()
                if metodo in ["brute", "rl"]:
                    df = df.loc[df['resultado'] == True]
                    canonical_time_aux = df[['G6', 'canonical_time']].groupby(['G6']).mean().reset_index()
                    solve_time_aux = df[['G6', 'solve_time']].groupby(['G6']).mean().reset_index()
                    df_time[metodo] = canonical_time_aux['canonical_time'] + solve_time_aux['solve_time']
                    # df[metodo] = df["canonical_time"] + df["solve_time"]
                else:
                    df_time[metodo] = df["PLI_create_time"] + df["solve_time"]
                # df[metodo] = df["canonical_time"] + df["solve_time"]
                # df[metodo] = df["solve_time"]
                # df[metodo] = df["qtde_moves"]

                df = df_time[[metodo]]
                df = df.to_dict("list")

                auxiliar[tamanho_grafico] = df[metodo]
            for i in range(10, 90, 10):
                box_plot_all[metodo].append(auxiliar[str(i)])


box_plot_all['RL'] = sum(box_plot_all['rl'], [])
box_plot_all['Algoritmo de Busca'] = sum(box_plot_all['brute'], [])
# box_plot_all['direct'] = sum(box_plot_all['direct'], [])

del box_plot_all['rl']
del box_plot_all['brute']

data = pd.DataFrame(box_plot_all)

data_long = pd.melt(data, id_vars=['Número de vértices'], var_name='Método', value_name='Tempo (s)')

ax = sns.boxplot(x='Número de vértices', y='Tempo (s)', hue='Método', data=data_long)
ax.set_axisbelow(True) 
plt.grid(True, color='lightgray', linestyle='-', linewidth=0.7)
# for patch, color in zip(ax.patches, ["blue", "red"]):
'''
colors = ["blue", "orange"]
for patch, color in zip(ax.patches, colors*9):
    patch.set_facecolor(color)
# Adiciona uma legenda personalizada
custom_legend = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(custom_legend, ["RL", "Algoritmo de Busca"], title="Método")
'''

# plt.title('Comparação de distribuições por tamanho de grafo', fontsize=12)
# plt.ylim(0, 1.8)
# plt.yticks(np.arange(0, 2, 0.2)) 
# plt.savefig('boxplot_benchmark_all_sem_ilp.png', format='png', dpi=300, bbox_inches='tight')

plt.savefig('boxplot_benchmark_all_sem_ilp.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
print()


#'''