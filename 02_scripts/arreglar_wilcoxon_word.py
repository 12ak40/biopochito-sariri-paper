from docx import Document
import os

doc_path = "05_manuscript/Paper.docx"

if not os.path.exists(doc_path):
    print(f"ERROR: No se encuentra {doc_path}.")
    exit()

doc = Document(doc_path)

# --- REEMPLAZO DE TEXTO (Sección 3.2 y 2.6) ---
# Buscamos el párrafo de resultados antiguo para reemplazarlo por el nuevo
nuevo_texto_3_2 = (
    "Because the assumption of normality was violated for all difference scores (Shapiro-Wilk p < 0.05), "
    "the non-parametric Wilcoxon signed-rank test was used. Table 1 presents the pre- and post-test results "
    "using medians and interquartile ranges (IQR). The Wilcoxon signed-rank test revealed statistically "
    "significant short-term improvements after Bonferroni correction (p < 0.0125) in Knowledge (W = 113.0, "
    "p < 0.0001, r = +0.78), Environmental Attitude (W = 168.0, p = 0.0053, r = +0.52), and Curiosity "
    "(W = 214.0, p = 0.0077, r = +0.48). For these three constructs, the number of participants who improved (+), "
    "worsened (-), or showed no change (0) were 38/7/7, 27/10/15, and 29/11/12, respectively. MIL Self-Efficacy "
    "showed a positive nominal change (W = 396.0, p = 0.0477, r = +0.33), with 30 participants improving, 18 worsening, "
    "and 4 remaining unchanged; however, this result did not meet the corrected significance threshold. The 95% "
    "confidence intervals for the median differences are detailed in Table 1."
)

for p in doc.paragraphs:
    # Actualizar Sección 2.6 (Tamaño del efecto)
    if "Effect sizes were calculated using the rank-biserial correlation" in p.text:
        p.text = ("Effect sizes were calculated using the signed rank-biserial correlation (r). Medians and "
                  "interquartile ranges (IQR) were used as descriptive statistics. The 95% confidence intervals (CI) "
                  "for the median differences were calculated using a bootstrap approach (2000 resamples). The number "
                  "of positive, negative, and zero differences were also recorded.")
    
    # Actualizar Sección 3.2 (Resultados)
    if "Table 1 presents the pre- and post-test results" in p.text:
        p.text = nuevo_texto_3_2

# --- ACTUALIZACIÓN DE LA TABLA 1 ---
for table in doc.tables:
    if len(table.columns) == 7 and "Wilcoxon W" in table.rows[0].cells[4].text:
        # 1. Cambiar cabeceras
        table.rows[0].cells[0].text = "Construct"
        table.rows[0].cells[1].text = "Pre Median (IQR)"
        table.rows[0].cells[2].text = "Post Median (IQR)"
        table.rows[0].cells[3].text = "Median Diff [95% CI]"
        table.rows[0].cells[4].text = "+ / - / 0"
        table.rows[0].cells[5].text = "W (W+ / W-)"
        table.rows[0].cells[6].text = "p-value & Effect size"

        # 2. Fila 1: Knowledge
        table.rows[1].cells[1].text = "6.0 (3.2)"
        table.rows[1].cells[2].text = "8.0 (3.0)"
        table.rows[1].cells[3].text = "+2.0 [1.0, 3.0]"
        table.rows[1].cells[4].text = "38 / 7 / 7"
        table.rows[1].cells[5].text = "113.0 (922.0 / 113.0)"
        table.rows[1].cells[6].text = "< 0.0001* | r = +0.78"

        # 3. Fila 2: Environmental Attitude
        table.rows[2].cells[1].text = "21.0 (5.2)"
        table.rows[2].cells[2].text = "22.0 (4.2)"
        table.rows[2].cells[3].text = "+1.0 [0.0, 1.5]"
        table.rows[2].cells[4].text = "27 / 10 / 15"
        table.rows[2].cells[5].text = "168.0 (535.0 / 168.0)"
        table.rows[2].cells[6].text = "0.0053* | r = +0.52"

        # 4. Fila 3: Curiosity
        table.rows[3].cells[1].text = "20.0 (5.5)"
        table.rows[3].cells[2].text = "21.0 (5.0)"
        table.rows[3].cells[3].text = "+1.0 [0.0, 1.0]"
        table.rows[3].cells[4].text = "29 / 11 / 12"
        table.rows[3].cells[5].text = "214.0 (606.0 / 214.0)"
        table.rows[3].cells[6].text = "0.0077* | r = +0.48"

        # 5. Fila 4: MIL Self-Efficacy
        table.rows[4].cells[1].text = "30.0 (7.0)"
        table.rows[4].cells[2].text = "30.0 (7.2)"
        table.rows[4].cells[3].text = "0.0 [0.0, 2.0]"
        table.rows[4].cells[4].text = "30 / 18 / 4"
        table.rows[4].cells[5].text = "396.0 (780.0 / 396.0)"
        table.rows[4].cells[6].text = "0.0477 | r = +0.33"
        
        # 6. Nota de la tabla (Asegúrate de que la última fila sea la nota)
        try:
            last_row = table.rows[-1]
            last_row.cells[0].text = "Note: Values are medians with interquartile ranges (IQR). Differences are Post minus Pre. + / - / 0 indicates the number of participants who improved, worsened, or showed no change. W represents the Wilcoxon signed-rank statistic. Effect size r is the signed rank-biserial correlation. *Significant after Bonferroni correction (p < 0.0125)."
        except:
            pass

        print("Tabla 1 y textos actualizados correctamente.")

doc.save("05_manuscript/Paper_wilcoxon.docx")
print("¡Éxito! Archivo guardado como 05_manuscript/Paper_wilcoxon.docx")
