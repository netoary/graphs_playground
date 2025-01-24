import pandas as pd

testes = {}

testes["brute"] = {
    "all": [
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/brute_5regular8-all_g6_2024_04_21_23.csv",
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/brute_5regular10-all_g6_2024_04_21_23.csv",
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/brute_5regular12-all_g6_2024_04_21_23.csv",
    ],
    "planar": [
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/brute_5reg_planar_16_g6_2024_04_21_23.csv",
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/brute_5reg_planar_18_g6_2024_04_21_23.csv",
    ],
    "bipartite": ["/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/brute_5reg_bipartite_14_g6_2024_07_11_20.csv",]
}

testes["angle"] = {
    "all": [
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/angle_ilp_5regular8-all_g6_2024_04_28_19.csv",
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/angle_ilp_5regular10-all_g6_2024_04_28_19.csv",
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/angle_ilp_5regular12-all_g6_2024_04_28_19.csv",
    ],
    "planar": [
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/angle_ilp_5reg_planar_16_g6_2024_04_28_15.csv",
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/angle_ilp_5reg_planar_18_g6_2024_05_01_23.csv",
    ],
    "bipartite": ["/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/angle_ilp_5reg_bipartite_14_g6_2024_07_14_14.csv",]
}

testes["direct"] = {
    "all": [
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/direct_ilp_5regular8-all_g6_2024_04_30_19.csv",
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/direct_ilp_5regular10-all_g6_2024_04_30_19.csv",
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/direct_ilp_5regular12-all_g6_2024_04_30_19.csv",
    ],
    "planar": [
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/direct_ilp_5reg_planar_16_g6_2024_04_29_20.csv",
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/direct_ilp_5reg_planar_18_g6_2024_04_29_20.csv",
    ],
    "bipartite": [
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/direct_ilp_5reg_bipartite_14_g6_2024_07_13_09.csv",
    ],
}

testes["rl"] = {
    "all": [
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/rl_5regular8-all_g6_2024_09_15_22.csv",
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/rl_5regular10-all_g6_2024_09_15_22.csv",
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/rl_5regular12-all_g6_2024_09_15_22.csv",
    ],
    "planar": [
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/rl_5reg_planar_16_g6_2024_04_26_01.csv",
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/rl_5reg_planar_18_g6_2024_04_26_01.csv",
    ],
    "bipartite": [
        "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/todos_rodaram/rl_5reg_bipartite_14_g6_2024_09_16_00.csv",
    ],
}

resultados = {
    "brute": {
        "all": [],
        "planar": [],
        "bipartite": [],
    },
    "angle": {
        "all": [],
        "planar": [],
        "bipartite": [],
    },
    "direct": {
        "all": [],
        "planar": [],
        "bipartite": [],
    },
    "rl": {
        "all": [],
        "planar": [],
        "bipartite": [],
    },
}

for metodo, teste in testes.items():
    for tipo, caminhos in teste.items():
        full_df = pd.DataFrame()
        for caminho in caminhos:
            df = pd.read_csv(caminho)
            
            if metodo in ["brute", "rl"]:
                df["total_time"] = df["canonical_time"] + df["solve_time"]
            else:
                df["total_time"] = df["PLI_create_time"] + df["solve_time"]
            full_df = pd.concat([full_df, df])

        numero_total_de_testes = len(df)

        tempo_medio = df["total_time"].mean()
        tempo_min = df["total_time"].min()
        tempo_max = df["total_time"].max()
        desvio_do_tempo_medio = df["total_time"].std()
        
        resultados[metodo][tipo].append(tempo_medio)
        resultados[metodo][tipo].append(desvio_do_tempo_medio)
        resultados[metodo][tipo].append(tempo_min)
        resultados[metodo][tipo].append(tempo_max)

print(resultados)