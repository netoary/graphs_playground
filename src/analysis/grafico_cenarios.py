import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math




caminho_base = '/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/separado/'

cenario = 'cenario1'

error_bar = '' # '_error_bar'

cenarios = {
    'cenario1': {
        # 'metodos': ["rl", "brute", "direct"],
        # 'metodos': ["rl", "brute"],
        'metodos': ["direct"],
        'x': [16, 18, 20, 22, 24, 26]
    },
    'cenario2': {
        # 'metodos': ["rl", "brute", "direct", "angle"],
        'metodos': ["direct", "angle"],
        # 'metodos': ["rl", "brute"],
        'x': [8, 10, 12]
    },
    'cenario3': {
        'metodos': ["rl", "brute"],
        # 'x': [14, 16, 18, 20]
        'x': [14, 16, 18]
    },
}



metodos = cenarios[cenario]['metodos']

testes = {}

for metodo in metodos:
    caminho_pasta = caminho_base + cenario + '/' + metodo
    testes[metodo] = {}

    for arquivo in os.listdir(caminho_pasta):
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        quebra = arquivo.split("_")
        testes[metodo][quebra[0]] = caminho_completo


all_results = {}
testes_label = ['rl_bipartite_benchmark_12', 'rl_bipartite_benchmark_04', 'rl_all_benchmark']
for metodo, teste_grafo in testes.items():
    # resultados = {key: [] for key in metodo.keys()}
    resultados_metodo = {}

    for tamanho_grafico, caminho in teste_grafo.items():
        df = pd.read_csv(caminho)
        if metodo in ["brute", "rl"]:
            df["total_time"] = df["canonical_time"] + df["solve_time"]
        else:
            df["total_time"] = df["PLI_create_time"] + df["solve_time"]

        tempo_medio = df["total_time"].mean()
        desvio_do_tempo_medio = df["total_time"].std()
        resultados_metodo[tamanho_grafico] = [tempo_medio, desvio_do_tempo_medio]
    all_results[metodo] = resultados_metodo

'''
### GRAFICO DE LINHA

x = cenarios[cenario]['x']

y_final = {}
yerr_final = {}
for metodo, d in all_results.items():
    y = [0] * len(x)
    yerr = [0] * len(x)
    for idx, value in enumerate(x):
        # y[idx] = math.log(d.get(str(value), [0])[0])
        y[idx] = d.get(str(value), [0])[0]
        yerr[idx] = d.get(str(value), [0,0])[1]
    yerr = [abs(yer) for yer in yerr]
    y_final[metodo] = y
    yerr_final[metodo] = yerr


fig = plt.figure()
# for metodo, y in y_all.items():
#     plt.errorbar(x, y, yerr=yerr_all[metodo], label=metodo)

if cenario == 'cenario1':
    if error_bar == '_error_bar':
        plt.errorbar(x, y_final['rl'], yerr=yerr_final['rl'], label='RL')
        plt.errorbar(x, y_final['brute'], yerr=yerr_final['brute'], label='Algorito 1')
        plt.errorbar(x, y_final['direct'], yerr=yerr_final['direct'], label='ILP Direto')
    else:
        plt.errorbar(x, y_final['rl'], label='RL', color='blue')
        plt.errorbar(x, y_final['brute'], label='Algoritmo de Busca', color='orange')
        plt.errorbar(x, y_final['direct'], label='ILP Direto', color='purple')

elif cenario == 'cenario2':
    if error_bar == '_error_bar':
        plt.errorbar(x, y_final['rl'], yerr=yerr_final['rl'], label='RL')
        plt.errorbar(x, y_final['brute'], yerr=yerr_final['brute'], label='Algorito 1')
        plt.errorbar(x, y_final['direct'], yerr=yerr_final['direct'], label='ILP Direto')
        plt.errorbar(x, y_final['angle'], yerr=yerr_final['angle'], label='ILP por Ângulos')
    else:
        plt.errorbar(x, y_final['rl'], label='RL', color='blue')
        plt.errorbar(x, y_final['brute'], label='Algoritmo de Busca', color='orange')
        plt.errorbar(x, y_final['direct'], label='ILP Direto', color='purple')
        plt.errorbar(x, y_final['angle'], label='ILP por Ângulos', color='brown')

else:
    if error_bar == '_error_bar':
        plt.errorbar(x, y_final['rl'], yerr=yerr_final['rl'], label='RL')
        plt.errorbar(x, y_final['brute'], yerr=yerr_final['brute'], label='Algorito 1')
    else:
        plt.errorbar(x, y_final['rl'], label='RL', color='blue')
        plt.errorbar(x, y_final['brute'], label='Algoritmo de Busca', color='orange')

plt.xlabel("Número de vértices")
plt.ylabel("Tempo (s)")
# plt.ylabel("Tempo log(s)")

plt.legend(loc='upper left')
# Ajustando o layout para evitar sobreposição
plt.xticks(x, x)
plt.tight_layout()
plt.grid(True, color='lightgray', linestyle='-', linewidth=0.7)
plt.savefig(f'line_graph_{cenario}{error_bar}.png', format='png', dpi=300, bbox_inches='tight')

plt.show()

print()

'''

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
    'Número de vértices': sum([[i]*10 for i in cenarios[cenario]['x']], []),
    # 'rl': [],
    # 'brute': [],
    'direct': [],
    # 'angle': [],
}

for metodo, teste_grafo in testes.items():
    auxiliar = {}
    for tamanho_grafico, caminho in teste_grafo.items():
        df = pd.read_csv(caminho)

        df_time = pd.DataFrame()
        if metodo in ["brute", "rl"]:
            canonical_time_aux = df[['G6', 'canonical_time']].groupby(['G6']).mean().reset_index()
            solve_time_aux = df[['G6', 'solve_time']].groupby(['G6']).mean().reset_index()
            df_time[metodo] = canonical_time_aux['canonical_time'] + solve_time_aux['solve_time']
            # df[metodo] = df["canonical_time"] + df["solve_time"]
        else:
            df_time[metodo] = (df["PLI_create_time"] + df["solve_time"]).apply(lambda x: math.log(x))
        # df[metodo] = df["canonical_time"] + df["solve_time"]
        # df[metodo] = df["solve_time"]
        # df[metodo] = df["qtde_moves"]

        df = df_time[[metodo]]
        df = df.to_dict("list")

        auxiliar[tamanho_grafico] = df[metodo]
    for i in cenarios[cenario]['x']:
        box_plot_all[metodo].append(auxiliar[str(i)])

# box_plot_all['Número de vértices'] = sum([[i]*len(box_plot_all['rl'][idx]) for idx, i in enumerate(cenarios[cenario]['x'])], [])
# box_plot_all['RL'] = sum(box_plot_all['rl'], [])
# box_plot_all['Algoritmo de Busca'] = sum(box_plot_all['brute'], [])

# del box_plot_all['rl']
# del box_plot_all['brute']

box_plot_all['Número de vértices'] = sum([[i]*len(box_plot_all['direct'][idx]) for idx, i in enumerate(cenarios[cenario]['x'])], [])
box_plot_all['ILP Direto'] = sum(box_plot_all['direct'], [])
# box_plot_all['ILP por Ângulos'] = sum(box_plot_all['angle'], [])

del box_plot_all['direct']
# del box_plot_all['angle']

data = pd.DataFrame(box_plot_all)

# data_long = pd.melt(data, id_vars=['Número de vértices'], var_name='Método', value_name='Tempo (s)')
# ax = sns.boxplot(x='Número de vértices', y='Tempo (s)', hue='Método', data=data_long)

data_long = pd.melt(data, id_vars=['Número de vértices'], var_name='Método', value_name='Tempo log(s)')
ax = sns.boxplot(x='Número de vértices', y='Tempo log(s)', hue='Método', data=data_long)
ax.set_axisbelow(True) 
# plt.title('Comparação de distribuições por tamanho de grafo', fontsize=12)
# plt.ylim(0, 1.8)
# plt.yticks(np.arange(0, 2, 0.2)) 

colors = ["purple"]
i = 0
for patch, color in zip(ax.patches, colors*7):
    # if i == 1:
    #     patch.set_facecolor("purple")
    # else:
    #     patch.set_facecolor(colors[i % 2])
    patch.set_facecolor(color)
    i += 1
# Adiciona uma legenda personalizada
custom_legend = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(custom_legend, ["ILP Direto"], title="Método")

plt.grid(True, color='lightgray', linestyle='-', linewidth=0.7)
plt.savefig(f'boxplot_{cenario}_ILP.png', format='png', dpi=300, bbox_inches='tight')
plt.show()
print()


#'''