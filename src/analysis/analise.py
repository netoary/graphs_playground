import pandas as pd

def resultado_brute_test():
    total_testes = {
        "brute_8": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5regular8-all_g6_2024_04_21_23.csv",
        "brute_10": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5regular10-all_g6_2024_04_21_23.csv",
        "brute_12": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/brute_5regular12-all_g6_2024_04_21_23.csv",
        "brute_16": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_16_g6_2024_04_26_01.csv",
        "brute_18": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_16_g6_2024_04_26_01.csv",
        "brute_20": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_16_g6_2024_04_26_01.csv",
        "brute_22": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_16_g6_2024_04_26_01.csv",
        "brute_24": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_16_g6_2024_04_26_01.csv",
        "brute_26": "/home/ary/Área de Trabalho/TCC/codigo_limpo_e_final/graphs_playground/outputs/rl_5reg_planar_16_g6_2024_04_26_01.csv",
    }

    resultados = {
        "brute_8": [],
        "brute_10": [],
        "brute_12": [],
        "brute_16": [],
        "brute_18": [],
        "brute_20": [],
        "brute_22": [],
        "brute_24": [],
        "brute_26": [],
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

print(resultados)