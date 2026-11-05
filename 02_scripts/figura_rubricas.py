import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargar datos verificados
df = pd.read_csv("01_data/processed/Rubric_Results_VERIFIED.csv")

# Configurar estilo básico
plt.figure(figsize=(8, 5))

# Separar datos por estación
b_scores = df[df['Station'] == 'B']['Mean_Score']
c_scores = df[df['Station'] == 'C']['Mean_Score']

# Crear boxplot
bp = plt.boxplot([b_scores, c_scores], tick_labels=['Station B\n(Stories & Art)', 'Station C\n(Video)'],                 
patch_artist=True, widths=0.4)

# Colores para las cajas
colors = ['#66c2a5', '#fc8d62']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Añadir los puntos individuales (jitter)
for i, scores in enumerate([b_scores, c_scores], start=1):
    # Jitter simple para que no se superpongan los puntos
    x_jitter = [i + (j * 0.02 - 0.3) for j in range(len(scores))] 
    plt.scatter(x_jitter, scores, color='black', alpha=0.5, s=30, zorder=3)

# Añadir los promedios como texto
means = [b_scores.mean(), c_scores.mean()]
for i, mean_val in enumerate(means, start=1):
    plt.text(i, mean_val + 0.1, f"Mean: {mean_val:.2f}", ha='center', va='bottom', fontweight='bold', fontsize=11)

plt.title("Artifact Scores by Station (1-4 scale)", fontsize=14)
plt.ylabel("Mean Score", fontsize=12)
plt.ylim(0.5, 4.5)
plt.grid(axis='y', linestyle='--', alpha=0.7)

os.makedirs("04_output/figures", exist_ok=True)
plt.tight_layout()
plt.savefig("04_output/figures/Figure_Rubrics_B_C.png", dpi=300)
print("Guardado: 04_output/figures/Figure_Rubrics_B_C.png")
