import pandas as pd
from scipy import stats
import io

# Los datos exactos que me enviaste, listos para ser procesados
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

# Cargamos los datos desde el string usando tabulación como separador
df = pd.read_csv(io.StringIO(datos), sep='\t')

# Limpiamos nombres de columnas
df.columns = df.columns.str.strip()

def calcular_totales(prefijo):
    # Sumar A (5 items)
    df[f'{prefijo}_TOTAL_A'] = df[[f'{prefijo}_A1', f'{prefijo}_A2', f'{prefijo}_A3', f'{prefijo}_A4', f'{prefijo}_A5']].apply(pd.to_numeric, errors='coerce').sum(axis=1)
    # Sumar B (8 items)
    df[f'{prefijo}_TOTAL_B'] = df[[f'{prefijo}_B1', f'{prefijo}_B2', f'{prefijo}_B3', f'{prefijo}_B4', f'{prefijo}_B5', f'{prefijo}_B6', f'{prefijo}_B7', f'{prefijo}_B8']].apply(pd.to_numeric, errors='coerce').sum(axis=1)
    # Sumar C (5 items)
    df[f'{prefijo}_TOTAL_C'] = df[[f'{prefijo}_C1', f'{prefijo}_C2', f'{prefijo}_C3', f'{prefijo}_C4', f'{prefijo}_C5']].apply(pd.to_numeric, errors='coerce').sum(axis=1)
    # Sumar D (8 items: D1-D4 son 0 o 1, D5-D8 son 0,1,2 según rúbrica)
    df[f'{prefijo}_TOTAL_D'] = df[[f'{prefijo}_D1', f'{prefijo}_D2', f'{prefijo}_D3', f'{prefijo}_D4', f'{prefijo}_D5', f'{prefijo}_D6', f'{prefijo}_D7', f'{prefijo}_D8']].apply(pd.to_numeric, errors='coerce').sum(axis=1)

calcular_totales('PRE')
calcular_totales('POST')

# Eliminar filas que tengan NaN en los totales
df = df.dropna(subset=['PRE_TOTAL_A', 'POST_TOTAL_A'])

print(f"📊 Análisis realizado con {len(df)} participantes válidos.\n")

def analizar(pre_col, post_col, nombre, max_score):
    pre = df[pre_col]
    post = df[post_col]
    
    # Prueba t pareada
    t_stat, p_val = stats.ttest_rel(post, pre)
    
    # Cohen's d
    diff = post - pre
    cohen_d = diff.mean() / diff.std() if diff.std() != 0 else 0
    
    print(f"--- {nombre} (Max: {max_score}) ---")
    print(f"Pre:  {pre.mean():.2f} ± {pre.std():.2f}")
    print(f"Post: {post.mean():.2f} ± {post.std():.2f}")
    print(f"Mejora: {post.mean() - pre.mean():+.2f}")
    print(f"Prueba t: t({len(df)-1}) = {t_stat:.2f}, p = {p_val:.4f}")
    print(f"Cohen's d: {cohen_d:.2f} ", end="")
    if p_val < 0.05:
        print("(Significativo ✅)\n")
    else:
        print("(No significativo ❌)\n")

analizar('PRE_TOTAL_A', 'POST_TOTAL_A', 'Curiosidad', 25)
analizar('PRE_TOTAL_B', 'POST_TOTAL_B', 'MIL Self-Efficacy', 40)
analizar('PRE_TOTAL_C', 'POST_TOTAL_C', 'Actitud Ambiental', 25)
analizar('PRE_TOTAL_D', 'POST_TOTAL_D', 'Conocimiento', 12)
