from docx import Document

doc = Document("05_manuscript/Paper.docx")

# 1. Arreglar Hardware
texto_hardware_nuevo = "Technically, Biopochito is an AI companion deployed on a custom, compact hardware device (dimensions: 4 × 4.5 × 2 cm). The device connects to the internet to process natural language and generate responses. To ensure safety, the system uses a rule-based Retrieval-Augmented Generation (RAG) architecture, retrieving facts from a curated, cloud-hosted database of approximately 500 text chunks focused on Lake Titicaca."

# 2. Arreglar Nota Tabla 1
nota_tabla1 = "Note: Values are presented as medians with interquartile ranges (IQR). Differences are calculated as Post minus Pre. The + / - / 0 column indicates the number of participants who improved, worsened, or showed no change, respectively. W represents the Wilcoxon signed-rank statistic, where W+ and W- indicate the sum of positive and negative ranks. Effect size r is the signed rank-biserial correlation, defined as (W+ - W-) / (W+ + W-). Zeros were discarded and ties were handled asymptotically (SciPy 1.13). *Significant after Bonferroni correction for the four primary outcomes (threshold p = 0.0125). 95% CI = Confidence Interval for the median difference (bootstrap, 2000 resamples)."

# 3. Financiamiento
texto_funding = "Funding: This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. The study was conducted using the institutional resources and in-kind support of the authors' affiliated organizations."

# 4. Contribuciones
texto_contrib = "Author Contributions: Conceptualization, M.A.C.Z.; methodology, M.A.C.Z., Y.A.S., J.G.P.C., and M.L.O.S.; software, M.A.C.Z.; validation, M.A.C.Z., Y.A.S., M.L.O.S., J.E.G.B., J.G.P.C., C.A.C.G., and M.S.; formal analysis, M.A.C.Z.; investigation, Y.A.S.; data curation, M.A.C.Z., G.A.J.A., and P.B.C.; writing—original draft preparation, M.A.C.Z.; writing—review and editing, all authors; supervision, M.A.C.Z. and Y.A.S.; project administration, M.A.C.Z. All authors have read and agreed to the published version of the manuscript."

# 5. Agradecimientos
texto_ack = "The authors express their deepest gratitude to Cecilia E. Pinedo, Director of Unidad Educativa Sariri, for her invaluable institutional support. We also thank the teachers Marco Antonio Viera, Daniela Gorena, and Santiago Blanco for their dedication to the observation protocol. We extend our appreciation to the faculty of Unidad Educativa Sariri, specifically Ezequiel Montiel Espejo, Magda Mamani Condori, and Antonio Mamani Nina, for their collaboration. Furthermore, we acknowledge the technical support and implementation team, Víctor Mamani, Mariela Castel, Naira Mercado, Irene Portocarrero, Madelein Gómez, and Damián Villegas, for their outstanding logistical support and assistance in organizing the event. Finally, we thank the students and families who participated in this study."

for p in doc.paragraphs:
    # 1. Hardware
    if "hosted locally on the tablets without internet access" in p.text or "Technically, Biopochito is a hybrid AI system" in p.text:
        p.text = texto_hardware_nuevo
        
    # 2. Nota Tabla 1
    elif "Significant after Bonferroni correction" in p.text or "Values are medians with interquartile" in p.text:
        p.text = nota_tabla1
        
    # 3. Financiamiento
    elif "The authors declare no conflict of interest" in p.text:
        p.text = p.text + "\n\n" + texto_funding
        
    # 4. Contribuciones
    elif "Conceptualization, M.A.C.Z." in p.text:
        p.text = texto_contrib
        
    # 5. Agradecimientos
    elif "The authors thank the students, families, and educators" in p.text or "Acknowledgements" in p.text:
        p.text = texto_ack

doc.save("05_manuscript/Paper.docx")
print("¡Éxito! Todas las alertas de la auditoría han sido corregidas.")
