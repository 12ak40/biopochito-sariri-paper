import pandas as pd
from scipy import stats

# (Pega aquí el bloque de datos 'datos = """..."""' tal como lo hicimos en el paso anterior)

df = pd.read_csv("01_data/raw/datos.txt", sep="\t")
df.columns = df.columns.str.strip()

def calcular_totales(prefijo):
    df[f'{prefijo}_TOTAL_A'] = df[[f'{prefijo}_A1', f'{prefijo}_A2', f'{prefijo}_A3', f'{prefijo}_A4', f'{prefijo}_A5']].apply(pd.to_numeric, errors='coerce').sum(axis=1)
    df[f'{prefijo}_TOTAL_B'] = df[[f'{prefijo}_B1', f'{prefijo}_B2', f'{prefijo}_B3', f'{prefijo}_B4', f'{prefijo}_B5', f'{prefijo}_B6', f'{prefijo}_B7', f'{prefijo}_B8']].apply(pd.to_numeric, errors='coerce').sum(axis=1)
    df[f'{prefijo}_TOTAL_C'] = df[[f'{prefijo}_C1', f'{prefijo}_C2', f'{prefijo}_C3', f'{prefijo}_C4', f'{prefijo}_C5']].apply(pd.to_numeric, errors='coerce').sum(axis=1)
    df[f'{prefijo}_TOTAL_D'] = df[[f'{prefijo}_D1', f'{prefijo}_D2', f'{prefijo}_D3', f'{prefijo}_D4', f'{prefijo}_D5', f'{prefijo}_D6', f'{prefijo}_D7', f'{prefijo}_D8']].apply(pd.to_numeric, errors='coerce').sum(axis=1)

calcular_totales('PRE')
calcular_totales('POST')

df = df.dropna(subset=['PRE_TOTAL_A', 'POST_TOTAL_A'])

# --- NUEVAS PRUEBAS: SHAPIRO-WILK & WILCOXON ---
def pruebas_avanzadas(pre_col, post_col, nombre):
    pre = df[pre_col]
    post = df[post_col]
    diff = post - pre
    
    # 1. Shapiro-Wilk en las diferencias
    shapiro_stat, shapiro_p = stats.shapiro(diff)
    
    # 2. Prueba t pareada
    t_stat, p_t = stats.ttest_rel(post, pre)
    
    # 3. Wilcoxon (Prueba de sensibilidad no paramétrica)
    wilcoxon_stat, p_wilcoxon = stats.wilcoxon(post, pre)
    
    print(f"\n--- {nombre} ---")
    print(f"Shapiro-Wilk (Diferencias): W = {shapiro_stat:.4f}, p = {shapiro_p:.4f}")
    if shapiro_p > 0.05:
        print("  -> Asunción de normalidad CUMPLIDA. (Usar prueba t).")
    else:
        print("  -> Asunción de normalidad VIOLADA. (Se requiere Wilcoxon).")
        
    print(f"Prueba T (Paramétrica):   t = {t_stat:.2f}, p = {p_t:.4f}")
    print(f"Prueba Wilcoxon (No Par): W = {wilcoxon_stat:.2f}, p = {p_wilcoxon:.4f}")

pruebas_avanzadas('PRE_TOTAL_A', 'POST_TOTAL_A', 'Curiosidad')
pruebas_avanzadas('PRE_TOTAL_B', 'POST_TOTAL_B', 'MIL Self-Efficacy')
pruebas_avanzadas('PRE_TOTAL_C', 'POST_TOTAL_C', 'Actitud Ambiental')
pruebas_avanzadas('PRE_TOTAL_D', 'POST_TOTAL_D', 'Conocimiento')
