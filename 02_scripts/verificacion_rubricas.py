import pandas as pd

df = pd.read_csv("01_data/processed/Rubric_Results_Sariri.csv")

# Calcular el promedio real (suma de criterios / 4)
df['Calculated_Mean'] = df[['Criterion_1', 'Criterion_2', 'Criterion_3', 'Criterion_4']].mean(axis=1)

# Detectar filas donde la columna manual del Word difiere del cálculo real (margen de 0.01 por redondeo)
df['Difference'] = abs(df['Mean_Score'] - df['Calculated_Mean'])
errors = df[df['Difference'] > 0.01]

print("=== ERRORES DE CÁLCULO EN EL DOCUMENTO DE WORD ===")
if len(errors) > 0:
    print(errors[['Station', 'Code_or_ID', 'Criterion_1', 'Criterion_2', 'Criterion_3', 'Criterion_4', 'Mean_Score', 'Calculated_Mean']].to_string(index=False))
else:
    print("No se encontraron errores.")

print("\n=== PROMEDIOS REALES (calculados desde criterios) ===")
for station in ['B', 'C']:
    sub = df[df['Station'] == station]
    mean_real = sub['Calculated_Mean'].mean()
    print(f"Estación {station}: N = {len(sub)}, Promedio = {mean_real:.4f}")

# Guardar el CSV limpio (con la columna calculada en lugar de la manual)
df_clean = df.drop(columns=['Mean_Score', 'Difference']).rename(columns={'Calculated_Mean': 'Mean_Score'})
df_clean['Mean_Score'] = df_clean['Mean_Score'].round(2)
df_clean.to_csv("01_data/processed/Rubric_Results_VERIFIED.csv", index=False)
print("\nGuardado: 01_data/processed/Rubric_Results_VERIFIED.csv")
