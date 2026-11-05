import pandas as pd

# Cargar datos
df = pd.read_csv("01_data/raw/datos.txt", sep="\t")
df.columns = df.columns.str.strip()

# Contar las frecuencias basadas en la rúbrica (usando los puntajes POST)
n_total = len(df)

# 1. Initial Curiosity: E1 == 1 (Pregunta simple)
curiosity = len(df[df['POST_E1'] == 1])

# 2. Causal Questioning: D5 >= 1 (Menciona una o más amenazas)
causal = len(df[df['POST_D5'] >= 1])

# 3. MIL Verification: E1 == 2 (Pregunta investigativa)
mil = len(df[df['POST_E1'] == 2])

# 4. Systems Thinking: D6 == 2 (Distinción clara) OR D8 == 2 (Acción específica)
systems = len(df[(df['POST_D6'] == 2) | (df['POST_D8'] == 2)])

print("=== VERIFICACIÓN TABLA 2 (POST-TEST) ===")
print(f"Total participantes: {n_total}")
print(f"Initial Curiosity (E1=1)      : {curiosity} ({(curiosity/n_total)*100:.1f}%)")
print(f"Causal Questioning (D5>=1)    : {causal} ({(causal/n_total)*100:.1f}%)")
print(f"MIL Verification (E1=2)       : {mil} ({(mil/n_total)*100:.1f}%)")
print(f"Systems Thinking (D6=2 | D8=2): {systems} ({(systems/n_total)*100:.1f}%)")
