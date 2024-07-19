import pandas as pd

# df = pd.read_csv("../outputs/brute_5reg_planar_16_g6_2024_04_21_23.csv")
brute_planar_16 = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5reg_planar_16_g6_2024_04_21_23.csv")
brute_planar_18 = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5reg_planar_18_g6_2024_04_21_23.csv")
brute_planar_20 = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5reg_planar_20_g6_2024_04_21_23.csv")
brute_planar_22 = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5reg_planar_22_g6_2024_04_21_23.csv")
brute_planar_24 = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5reg_planar_24_g6_2024_04_21_23.csv")
brute_planar_26 = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5reg_planar_26_g6_2024_04_21_23.csv")
rl_planar_16 = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_16_g6_2024_04_26_01.csv")
rl_planar_18 = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_18_g6_2024_04_26_01.csv")
rl_planar_20 = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_20_g6_2024_04_26_01.csv")
rl_planar_22 = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_22_g6_2024_04_26_01.csv")
rl_planar_24 = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_24_g6_2024_04_26_01.csv")
rl_planar_26 = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_26_g6_2024_04_26_01.csv")

# resultados = pd.read_csv("/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5reg_planar_26_g6_2024_04_21_23.csv")

brute_planar = pd.concat([brute_planar_16, brute_planar_18])
brute_planar = pd.concat([brute_planar, brute_planar_20])
brute_planar = pd.concat([brute_planar, brute_planar_22])
brute_planar = pd.concat([brute_planar, brute_planar_24])
brute_planar = pd.concat([brute_planar, brute_planar_26])
brute_planar = brute_planar.reset_index().drop(columns='index')

rl_planar = pd.concat([rl_planar_16, rl_planar_18])
rl_planar = pd.concat([rl_planar, rl_planar_20])
rl_planar = pd.concat([rl_planar, rl_planar_22])
rl_planar = pd.concat([rl_planar, rl_planar_24])
rl_planar = pd.concat([rl_planar, rl_planar_26])
rl_planar = rl_planar.reset_index().drop(columns='index')

brute_columns = {
    'G6': 'b_G6',
    'emparelhamento': 'b_emparelhamento',
    'canonical_time': 'b_canonical_time',
    'solve_time': 'b_solve_time',
    'qtde_moves': 'b_qtde_moves',
    'resultado': 'b_resultado',
    'max_depth': 'b_max_depth'
}

brute_planar = brute_planar.rename(columns=brute_columns)

rl_columns = {
    'G6': 'rl_G6',
    'emparelhamento': 'rl_emparelhamento',
    'canonical_time': 'rl_canonical_time',
    'solve_time': 'rl_solve_time',
    'qtde_moves': 'rl_qtde_moves',
    'resultado': 'rl_resultado',
    'max_depth': 'rl_max_depth'
}

rl_planar = rl_planar.rename(columns=rl_columns)

# resultados_negativos = resultados.loc[resultados['resultado'] == False]

# resultados = resultados.loc[resultados['resultado'] == True]

# resolvidos_dec_canonica = resultados.loc[resultados['qtde_moves'] == 0]
# resultados = resultados.loc[resultados['qtde_moves'] > 0]

# qtde_media_de_moves = resultados.groupby(['G6'])['qtde_moves'].mean()

# df = brute_planar_16.merge(rl_planar_16, on=['G6', 'emparelhamento'])
df = pd.concat([brute_planar, rl_planar], axis=1)

def calc_dif(x):
    if x['b_qtde_moves'] == 0:
        # return '-'
        return 0
    return x['rl_qtde_moves'] - x['b_qtde_moves']

df['diff'] = df.apply(lambda x: calc_dif(x), axis=1)
print()