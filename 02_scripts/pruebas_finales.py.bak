import pandas as pd
from scipy import stats
import io

# (Pega aquí el bloque de datos 'datos = """..."""' tal como lo hicimos en el paso anterior)
datos = """Codigo	PRE_A1	PRE_A2	PRE_A3	PRE_A4	PRE_A5	PRE_B1	PRE_B2	PRE_B3	PRE_B4	PRE_B5	PRE_B6	PRE_B7	PRE_B8	PRE_C1	PRE_C2	PRE_C3	PRE_C4	PRE_C5	PRE_D1	PRE_D2	PRE_D3	PRE_D4	PRE_D5	PRE_D6	PRE_D7	PRE_D8	PRE_E1	PRE_E2	POST_A1	POST_A2	POST_A3	POST_A4	POST_A5	POST_B1	POST_B2	POST_B3	POST_B4	POST_B5	POST_B6	POST_B7	POST_B8	POST_C1	POST_C2	POST_C3	POST_C4	POST_C5	POST_D1	POST_D2	POST_D3	POST_D4	POST_D5	POST_D6	POST_D7	POST_D8	POST_E1	POST_E2
SARIRI-001	5	5	5	5	4	3	5	5	4	5	4	5	2	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	5	5	5	5	4	3	5	5	5	5	4	5	4	5	5	5	5	5	1	0	1	1	1	0	1	1	0	0
SARIRI-002	5	5	5	4	5	4	5	5	5	4	5	3	4	5	4	5	5	5	0	0	1	0	0	0	0	1	1	2	5	4	5	5	5	4	5	5	4	5	5	4	4	5	4	5	5	5	0	1	1	1	0	0	0	2	1	1
SARIRI-003	5	5	4	5	5	1	5	3	1	5	5	1	1	5	5	5	3	5	0	1	0	0	1	1	0	1	1	1	5	5	5	5	5	1	1	3	2	5	5	1	5	5	5	5	1	5	1	0	1	1	1	0	0	1	1	0
SARIRI-004	5	5	5	5	5	5	4	5	5	3	5	5	5	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	3	5	3	5	5	3	3	5	5	3	5	1	5	5	5	5	5	3	1	0	1	0	1	0	0	0	0	0
SARIRI-005	5	5	5	5	5	5	5	5	5	5	4	5	3	5	5	5	5	3	1	0	0	1	1	0	1	1	2	0	5	5	5	5	5	5	5	5	5	4	5	5	5	5	5	5	5	5	1	1	1	1	1	2	1	1	1	2
SARIRI-006	5	5	4	5	5	4	3	5	5	5	5	4	5	5	5	5	5	5	0	0	1	0	1	1	1	1	1	1	5	5	4	5	5	4	5	5	5	5	5	4	5	5	5	5	5	5	1	0	1	1	1	1	1	1	1	1
SARIRI-007	4	3	0	1	0	3	3	4	5	5	5	5	4	5	3	5	5	5	0	0	1	0	2	0	0	2	2	0	5	3	5	1	5	3	4	5	5	5	5	5	5	5	5	5	5	5	0	0	0	1	1	0	0	0	0	0
SARIRI-008	5	4	5	4	5	4	4	5	4	5	5	3	1	5	5	5	5	4	0	0	0	0	1	0	1	1	1	1	5	4	5	4	5	5	4	5	4	4	5	4	4	5	4	3	4	5	0	1	1	1	0	0	1	1	1	1
SARIRI-009	5	4	5	3	5	3	4	3	3	5	1	3	3	5	4	5	5	4	0	1	0	0	1	0	1	1	0	0	5	4	4	5	5	4	3	3	3	4	1	3	3	5	5	5	4	5	0	0	1	1	1	1	0	1	0	0
SARIRI-010	2	1		4	4	3	3	1	4	4	3	3	3	5	4	5	3	4	0	0	0	0	0	0	0	0	1	0	5	5	5	5	5	0	0	4	4	5	5	3	0	5	5	0	4	3	0	0	0	1	0	0	0	1	0	0
SARIRI-011	5	4	4	3	5	4	3	3	4	4	4	3	1	5	4	5	4	3	0	0	1	1	0	0	0	1	1	1	5	4	4	3	5	3	3	3	4	5	4	3	2	5	4	5	4	3	1	0	1	1	1	0	0	2	1	2
SARIRI-012	4	5	5	4	5	4	4	5	4	3	4	3	4	5	4	5	5	3	0	0	1	1	0	0	0	0	0	0	4	5	4	4	5	1	3	4	3	4	4	3	4	5	4	5	4	3	1	1	1	1	0	0	1	1	1	0
SARIRI-013	5	5	5	5	5	4	5	5	5	5	4	5	4	5	5	5	5	5	1	1	1	1	1	0	1	0	1	1	5	5	5	5	5	5	5	5	5	5	5	5	5	5	5	5	5	5	1	0	1	1	1	0	2	0	1	1
SARIRI-014	1	5	4	5	5	2	1	5	4	1	1	5	1	5	4	5	5	5	1	0	0	0	0	0	0	0	0	0	5	5	5	5	5	1	3	5	1	1	5	5	1	5	5	5	5	5	1	0	0	1	0	0	1	1	0	2
SARIRI-015	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	3	3	4	4	4	3	3	4	3	4	4	3	3	4	4	4	4	4	1	1	1	1	2	2	2	2	2	2
SARIRI-016	2	3	4	2	1	3	3	3	3	2	4	4	2	4	4	2	3	2	1	1	1	1	1	1	1	2	0	2	2	4	2	3	1	2	3	2	3	1	3	2	2	4	5	3	3	1	1	1	0	1	0	0	0	1	1	0
SARIRI-017	4	4	4	4	5	4	4	3	4	4	5	5	5	5	5	4	5	5	1	1	0	1	0	2	1	2	1	1	5	4	5	4	5	4	4	4	5	5	5	5	5	5	5	5	5	5	1	1	1	1	1	2	1	2	1	1
SARIRI-018	4	3	3	2	4	4	4	4	3	2	3	3	3	0	0	0	0	0	1	1	0	1	0	1	1	2	1	2	3	4	4	4	4	3	0	4	3	3	4	4	4	4	4	4	4	4	1	1	0	1	1	1	0	1	2	1
SARIRI-019	3	5	4	4	3	3	5	5	3	1	2	5	5	5	5	5	5	5	1	0	0	1	1	1	1	2	2	1	5	4	5	5	5	3	3	5	4	5	3	5	5	5	5	5	5	5	1	1	1	1	1	2	1	2	1	1
SARIRI-020	4	3	5	2	5	3	3	4	3	1	3	4	3	5	3	4	4	5	1	1	0	1	1	0	0	0	2	0	2	4	4	2	5	3	3	2	3	1	3	3	3	5	4	4	3	4	1	1	1	1	0	0	0	0	0	0
SARIRI-021	4	4	4	3	5	3	3	4	4	5	5	4	4	5	5	5	5	5	1	1	0	1	1	1	1	1	2	1	5	5	5	5	5	4	4	5	5	5	5	4	5	5	5	5	5	5	1	1	1	1	1	1	1	1	1	1
SARIRI-022	2	3	5	2	2	5	4	3	4	3	4	4	5	5	4	4	4	4	1	0	0	0	1	1	1	2	2	1	4	4	4	2	4	4	4	3	4	3	4	4	5	5	4	4	4	4	1	1	1	1	1	0	0	0	0	0
SARIRI-023	2	4	5	1	3	3	4	2	3	4	5	4	5	4	5	3	2	1	1	0	0	0	1	1	1	1	1	1	2	4	4	1	1	3	3	2	4	4	2	5	1	3	5	5	3	1	1	1	1	1	1	1	1	1	2	1
SARIRI-024	3	5	5	3	5	4	5	0	5	4	5	4	4	5	5	5	4	5	1	1	0	1	0	2	1	2	1	1	5	4	5	3	5	5	4	4	5	5	5	4	4	5	5	5	5	5	1	1	1	1	2	2	1	1	2	1
SARIRI-025	4	5	4	3	4	3	4	4	4	5	3	5	5	5	5	5	4	5	1	0	0	1	1	1	1	1	2	1	4	5	5	3	4	3	4	4	5	5	4	3	5	5	5	5	5	5	1	1	1	1	1	1	1	1	1	1
SARIRI-026	4	5	4	3	3	3	3	2	2	3	4	3	3	4	5	4	4	5	0	1	0	1	2	2	2	2	2	2	4	5	5	2	3	3	3	2	3	5	2	4	3	4	4	5	4	4	1	1	1	1	2	2	1	1	0	1
SARIRI-027	3	4	4	3	3	2	2	2	2	3	3	3	3	4	4	3	2	4	1	0	0	1	1	2	1	2	2	2	2	3	4	1	5	2	3	3	3	4	4	3	4	5	5	5	5	5	1	1	1	1	1	1	1	2	0	1
SARIRI-028	4	4	4	3	3	3	1	4	3	4	3	3	4	4	3	4	3	4	0	1	0	0	1	1	1	1	1	1	4	3	4	3	4	3	4	3	4	5	3	3	2	5	3	4	5	3	0	1	1	1	1	1	1	2	0	0
SARIRI-029	3	4	5	4	4	1	3	1	4	5	4	4	4	5	5	4	3	4	0	0	0	1	1	1	1	1	2	1	4	4	5	3	3	2	3	2	5	4	4	3	3	5	5	4	4	5	0	1	0	1	2	1	1	1	1	1
SARIRI-030	5	5	3	1	5	2	5	5	4	3	5	5	4	1	5	4	5	3	0	1	0	0	0	0	1	0	0	1	3	5	5	4	5	3	4	4	3	4	4	3	5	5	4	4	5	3	1	1	0	1	0	1	2	2	0	1
SARIRI-031	3	4	3	2	3	3	4	3	3	5	4	4	4	5	4	3	4	3	1	0	0	0	1	2	2	2	0	1	2	3	3	2	3	3	4	4	3	5	3	4	4	5	4	3	4	3	1	1	0	1	1	2	2	2	0	1
SARIRI-032	3	3	4	3	4	5	5	4	2	2	2	5	3	5	2	3	3	3	1	0	0	1	1	1	1	1	1	1	2	3	4	3	4	4	5	4	3	2	2	4	3	4	2	2	2	3	1	1	1	1	1	1	1	1	0	1
SARIRI-033	3	5	5	4	3	5	4	4	5	4	4	5	5	4	5	3	5	3	1	1	0	1	1	2	1	1	2	1	5	5	5	5	3	5	5	4	5	4	5	5	5	4	5	3	5	3	1	1	1	1	2	2	1	2	1	1
SARIRI-034	2	4	4	4	3	3	1	4	3	4	2	3	4	4	3	4	3	4	0	1	0	0	1	1	1	2	1	2	3	4	4	3	4	3	4	3	4	5	3	3	2	5	3	4	5	3	0	1	1	1	1	1	2	1	0	0
SARIRI-035	2	4	5	4	3	3	1	4	3	4	2	3	4	4	3	4	3	4	0	1	0	0	1	1	1	1	1	1	3	4	5	4	3	3	5	4	5	5	4	5	4	5	5	4	5	5	0	1	0	1	2	1	1	1	2	1
SARIRI-036	4	3	4	3	2	4	5	3	4	4	4	5	3	5	4	3	4	4	0	1	0	0	1	0	1	1	0	0	4	4	4	3	3	5	5	3	4	4	3	4	2	5	4	4	5	4	0	1	1	1	2	0	1	1	2	1
SARIRI-037	4	5	5	4	5	4	4	5	3	3	5	4	3	5	5	3	3	3	1	1	0	1	1	1	1	1	2	2	5	4	5	4	4	3	3	4	3	4	4	4	4	5	5	5	5	4	1	1	1	1	1	2	2	2	2	2
SARIRI-038	4	5	5	4	5	3	4	4	4	3	4	4	1	5	5	4	4	2	0	1	0	1	1	0	1	1	2	1	5	5	5	5	5	4	4	4	5	3	3	4	3	5	5	4	5	3	1	1	1	1	1	1	1	1	2	1
SARIRI-039	4	3	3	2	3	3	4	5	4	5	3	2	4	5	4	3	4	4	0	1	0	0	1	1	1	1	2	1	4	3	4	2	3	4	3	5	4	3	3	4	2	5	4	2	3	4	1	1	1	1	1	1	1	1	2	1
SARIRI-040	3	4	5	2	2	3	5	3	4	4	2	4	1	3	4	3	4	3	0	1	0	1	1	1	1	1	2	1	3	4	5	5	3	4	3	4	3	2	2	3	3	5	4	5	4	5	1	1	1	1	1	1	1	1	2	1
SARIRI-041	4	5	4	3	5	3	4	5	5	4	3	4	3	5	4	4	4	5	1	0	0	1	0	1	1	1	2	1	5	4	5	4	4	4	4	5	3	5	3	3	3	5	4	3	3	3	1	1	1	1	0	1	1	0	1	1
SARIRI-042	4	3	4	3	3	4	5	3	5	4	4	4	3	4	3	3	3	2	1	1	0	1	1	1	1	1	0	1	4	3	4	3	4	4	5	3	4	3	4	4	3	5	4	3	4	3	1	1	0	1	1	0	1	1	0	1
SARIRI-043	3	4	3	2	3	3	3	2	3	4	4	3	5	5	5	5	3	4	0	0	0	0	2	1	1	2	2	2	4	4	3	4	5	4	3	4	5	5	4	3	4	5	5	4	3	5	1	1	1	1	1	1	1	2	2	1
SARIRI-044	4	3	5	3	5	3	3	4	4	3	3	3	3	4	3	4	4	4	1	1	1	1	2	1	1	2	2	1	4	3	3	3	4	3	3	3	4	3	4	3	4	4	3	4	4	4	1	1	1	1	1	1	1	1	2	1
SARIRI-045	4	4	5	3	5	3	4	3	4	4	4	4	4	5	5	4	4	4	1	1	1	1	2	2	2	2	2	2	4	4	5	4	5	4	4	4	5	4	4	4	5	5	4	4	5	4	1	1	1	1	2	2	2	2	2	2
SARIRI-046	4	3	5	4	4	3	4	3	4	4	4	4	4	4	4	4	4	4	1	1	1	1	2	2	2	0	2	1	4	5	4	3	5	4	3	4	5	5	4	3	5	5	5	4	3	4	1	1	1	1	1	1	1	2	2	1
SARIRI-047	5	5	5	3	5	3	3	2	4	4	4	2	3	5	5	5	5	4	0	1	0	1	2	1	1	2	1	1	5	3	5	3	5	4	3	3	3	4	4	3	4	5	5	5	5	4	0	1	0	1	2	1	1	2	2	1
SARIRI-048	5	5	5	3	5	3	3	3	4	3	3	3	3	5	5	5	5	5	0	0	0	1	1	1	1	1	2	1	5	5	5	3	5	3	3	3	3	3	3	3	3	5	5	5	5	5	0	1	1	1	1	1	1	2	1	1
SARIRI-049	3	4	3	5	5	3	4	5	3	3	4	5	3	5	4	5	3	4	1	1	1	1	1	2	1	1	2	0	5	4	5	3	4	4	4	5	3	3	4	5	4	5	4	5	5	4	1	1	1	1	1	2	1	2	2	1
SARIRI-050	4	3	5	4	5	3	5	5	4	3	4	5	4	5	5	5	4	5	1	1	1	1	2	2	1	2	2	1	4	4	5	4	5	3	4	5	4	4	4	5	4	5	5	4	5	5	1	1	1	1	2	2	1	2	1	1
SARIRI-051	3	2	1	2	3	1	3	2	3	2	2	3	3	5	4	3	4	3	1	0	0	1	1	1	1	1	2	1	3	2	2	2	3	2	3	2	2	2	3	3	3	5	4	3	3	3	1	1	1	1	1	2	1	1	2	1
SARIRI-052	4	5	5	3	5	4	5	3	4	4	3	3	3	5	4	4	5	4	1	0	0	1	1	1	1	1	2	1	5	4	4	5	4	4	4	3	4	5	4	3	3	5	5	5	5	3	0	1	1	1	1	1	0	1	0	0"""

df = pd.read_csv(io.StringIO(datos), sep='\t')
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
