import pandas as pd

INTERVAL_STEP = 100

def cluster_type(value):
    for i in range(INTERVAL_STEP):
        if value < (i + 1) * step:
            return i


df_brute_test_12_all = pd.read_csv("tests/brute_test_5regular12-all.g6.csv")

df_brute_test_12_all['tempo_total'] = df_brute_test_12_all['canonical_time'] + df_brute_test_12_all['solve_time']


df_ilp_direct_test_12_all = pd.read_csv("tests/direct_ilp_callback_test_5regular12-all.g6.csv")

df_ilp_direct_test_12_all['tempo_total'] = df_ilp_direct_test_12_all['PLI_create_time'] + df_ilp_direct_test_12_all['solve_time']


df_ilp_angle_test_12_all = pd.read_csv("tests/angle_ilp_callback_test_5regular12-all.g6.csv")

df_ilp_angle_test_12_all['tempo_total'] = df_ilp_angle_test_12_all['PLI_create_time'] + df_ilp_angle_test_12_all['solve_time']


max_brute = df_brute_test_12_all['tempo_total'].max()
max_direto = df_ilp_direct_test_12_all['tempo_total'].max()
max_angulo = df_ilp_angle_test_12_all['tempo_total'].max()

min_brute = df_brute_test_12_all['tempo_total'].min()
min_direto = df_ilp_direct_test_12_all['tempo_total'].min()
min_angulo = df_ilp_angle_test_12_all['tempo_total'].min()

mean_brute = df_brute_test_12_all['tempo_total'].mean()
mean_direto = df_ilp_direct_test_12_all['tempo_total'].mean()
mean_angulo = df_ilp_angle_test_12_all['tempo_total'].mean()

step_brute = (max_brute - min_brute) / INTERVAL_STEP
step_direct = (max_direto - min_direto) / INTERVAL_STEP
step_angle = (max_angulo - min_angulo) / INTERVAL_STEP

step = step_brute

print(f'\n\nMAX: \nBrute: {max_brute}\nDireto: {max_direto}\nAngulo: {max_angulo}')

print(f'\n\nMIN: \nBrute: {min_brute}\nDireto: {min_direto}\nAngulo: {min_angulo}')

print(f'\n\nMEAN: \nBrute: {mean_brute}\nDireto: {mean_direto}\nAngulo: {mean_angulo}')

print(f'\n\nSTEP: \nBrute: {step_brute}\nDireto: {step_direct}\nAngulo: {step_angle}')

df_brute_test_12_all['cluster'] = df_brute_test_12_all['tempo_total'].apply()

