import pandas as pd
from scipy import stats
import numpy as np

# 1. Cargar los datos
# Usamos 'sep="\t"' porque el archivo está separado por tabulaciones
try:
    df = pd.read_csv('datos.txt', sep=r'\s+', engine='python')
    print("✅ Datos cargados correctamente.")
except Exception as e:
    print("❌ Error al cargar el archivo:", e)
    exit()

# Limpiar posibles espacios en blanco en los nombres de las columnas
df.columns = df.columns.str.strip().str.replace('"', '').str.replace("'", "")
df = df.dropna(how='all')

# Eliminar filas vacías o sin código
df = df.dropna(subset=[df.columns[0]])

# 2. Definir las columnas y calcular totales
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

# Eliminar filas que tengan NaN en los totales (para no romper la prueba t)
df = df.dropna(subset=['PRE_TOTAL_A', 'POST_TOTAL_A'])

print(f"📊 Análisis realizado con {len(df)} participantes válidos.\n")

# 3. Función para calcular estadísticas
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

# 4. Ejecutar el análisis
analizar('PRE_TOTAL_A', 'POST_TOTAL_A', 'Curiosidad', 25)
analizar('PRE_TOTAL_B', 'POST_TOTAL_B', 'MIL Self-Efficacy', 40)
analizar('PRE_TOTAL_C', 'POST_TOTAL_C', 'Actitud Ambiental', 25)
analizar('PRE_TOTAL_D', 'POST_TOTAL_D', 'Conocimiento', 12)
