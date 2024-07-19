import pandas as pd

def resultado_brute_test():
    total_testes = {
        "brute_10": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_all_10_g6_2024_07_15_21.csv",
        "brute_20": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_all_20_g6_2024_07_15_21.csv",
        "brute_30": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_all_30_g6_2024_07_15_21.csv",
        "brute_40": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_all_40_g6_2024_07_15_21.csv",
        "brute_50": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_all_50_g6_2024_07_15_21.csv",
        "brute_60": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_all_60_g6_2024_07_15_21.csv",
        "brute_70": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_all_70_g6_2024_07_15_21.csv",
        "brute_80": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_all_80_g6_2024_07_15_21.csv",
        "brute_birpartite_10": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_birpartite_10_g6_2024_07_16_21.csv",
        "brute_birpartite_20": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_birpartite_20_g6_2024_07_16_21.csv",
        "brute_birpartite_30": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_birpartite_30_g6_2024_07_16_21.csv",
        "brute_birpartite_40": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_birpartite_40_g6_2024_07_16_21.csv",
        "brute_birpartite_50": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_birpartite_50_g6_2024_07_16_21.csv",
        "brute_birpartite_60": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_birpartite_60_g6_2024_07_16_21.csv",
        "brute_birpartite_70": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_birpartite_70_g6_2024_07_16_21.csv",
    }

    resultados = {
        "brute_10": [],
        "brute_20": [],
        "brute_30": [],
        "brute_40": [],
        "brute_50": [],
        "brute_60": [],
        "brute_70": [],
        "brute_80": [],
        "brute_birpartite_10": [],
        "brute_birpartite_20": [],
        "brute_birpartite_30": [],
        "brute_birpartite_40": [],
        "brute_birpartite_50": [],
        "brute_birpartite_60": [],
        "brute_birpartite_70": [],
    }

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
    return resultados

def resultado_angle_test():
    total_testes = {
        "angle_8": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/angle_ilp_5regular8-all_g6_2024_04_28_19.csv",
        "angle_10": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/angle_ilp_5regular10-all_g6_2024_04_28_19.csv",
        "angle_12": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/angle_ilp_5regular12-all_g6_2024_04_28_19.csv",
        "angle_16": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/angle_ilp_5reg_planar_16_g6_2024_04_28_15.csv",
        "angle_18": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/angle_ilp_5reg_planar_18_g6_2024_05_01_23.csv",
    }

    resultados = {
        "angle_8": [],
        "angle_10": [],
        "angle_12": [],
        "angle_16": [],
        "angle_18": [],
    }

    for teste, caminho in total_testes.items():
        df = pd.read_csv(caminho)

        numero_total_de_testes = len(df)
        numero_solucoes = len(df.loc[df["result"] == True])

        razao_de_solucoes = round((numero_solucoes / numero_total_de_testes * 100), 1)

        total_de_grafos_resolvidos = len(df[["G6"]].loc[df["result"] == True].drop_duplicates())


        df["total_time"] = df["PLI_create_time"] + df["solve_time"]

        tempo_medio = df["total_time"].mean()
        desvio_do_tempo_medio = df["total_time"].std()
        
        resultados[teste].append(tempo_medio)
        resultados[teste].append(desvio_do_tempo_medio)
        resultados[teste].append(razao_de_solucoes)
        resultados[teste].append(total_de_grafos_resolvidos)

def resultado_direct_test():
    total_testes = {
        "direct_8": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/direct_ilp_5regular8-all_g6_2024_04_30_19.csv",
        "direct_10": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/direct_ilp_5regular10-all_g6_2024_04_30_19.csv",
        "direct_12": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/direct_ilp_5regular12-all_g6_2024_04_30_19.csv",
        "direct_16": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/direct_ilp_5reg_planar_16_g6_2024_04_29_20.csv",
        "direct_18": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/direct_ilp_5reg_planar_18_g6_2024_04_29_20.csv",
        "direct_20": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/direct_ilp_5reg_planar_20_g6_2024_04_29_20.csv",
        "direct_22": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/direct_ilp_5reg_planar_22_g6_2024_04_29_20.csv",
        "direct_24": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/direct_ilp_5reg_planar_24_g6_2024_04_29_20.csv",
        # "direct_26": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_16_g6_2024_04_26_01.csv",
    }

    resultados = {
        "direct_8": [],
        "direct_10": [],
        "direct_12": [],
        "direct_16": [],
        "direct_18": [],
        "direct_20": [],
        "direct_22": [],
        "direct_24": [],
        "direct_26": [],
    }

    for teste, caminho in total_testes.items():
        df = pd.read_csv(caminho)

        numero_total_de_testes = len(df)
        numero_solucoes = len(df.loc[df["result"] == True])

        razao_de_solucoes = round((numero_solucoes / numero_total_de_testes * 100), 1)

        total_de_grafos_resolvidos = len(df[["G6"]].loc[df["result"] == True].drop_duplicates())


        df["total_time"] = df["PLI_create_time"] + df["solve_time"]

        tempo_medio = df["total_time"].mean()
        desvio_do_tempo_medio = df["total_time"].std()
        
        resultados[teste].append(tempo_medio)
        resultados[teste].append(desvio_do_tempo_medio)
        resultados[teste].append(razao_de_solucoes)
        resultados[teste].append(total_de_grafos_resolvidos)

def resultado_rl_test():
    total_testes = {
        # "rl_8": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5regular8-all_g6_2024_04_21_23.csv",
        # "rl_10": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5regular10-all_g6_2024_04_21_23.csv",
        # "rl_12": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5regular12-all_g6_2024_04_21_23.csv",
        "rl_16": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_16_g6_2024_04_26_01.csv",
        "rl_18": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_18_g6_2024_04_26_01.csv",
        "rl_20": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_20_g6_2024_04_26_01.csv",
        "rl_22": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_22_g6_2024_04_26_01.csv",
        "rl_24": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_24_g6_2024_04_26_01.csv",
        "rl_26": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_26_g6_2024_04_26_01.csv",
    }

    resultados = {
        "rl_8": [],
        "rl_10": [],
        "rl_12": [],
        "rl_16": [],
        "rl_18": [],
        "rl_20": [],
        "rl_22": [],
        "rl_24": [],
        "rl_26": [],
    }

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

resultados = resultado_brute_test()

print(resultados)