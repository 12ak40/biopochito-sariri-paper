from docx import Document
import os

# 1. DATOS COMUNES
autores = "Marco A. Cabero Z.¹,⁴,⁵, Yelka Aguilera S.¹,³,⁴,⁵, José G. Pérez C.²,⁴,⁵, Mary L. Ojeda S.²,⁴,⁵, Jorge E. Guevara B.¹,²,⁴, Moiya Sullivan¹,⁴,⁵, Gabriel A. Jimenez A.¹,⁴,⁵, Pablo Baldiviezo C.¹,⁴,⁵, Christian A. Cuero G.¹,²,⁴"
afiliaciones = [
    "¹ Andean Road Countries for Science and Technology (ARCST), Beijing, China",
    "² Unidad Central del Valle del Cauca (UCEVA), Tuluá, Colombia",
    "³ Universidad Privada del Valle, La Paz, Bolivia",
    "⁴ Science Culture Construction Research Institute, Cochabamba, Bolivia",
    "⁵ Journal of Latin American Sciences and Culture, Bolivia"
]
correspondencia = "Correspondence: marco.cabero@arcst.org"

acknowledgements = "The authors express their deepest gratitude to Cecilia E. Pinedo, Director of Unidad Educativa Sariri, for her invaluable institutional support. We also thank the teachers Marco Antonio Viera, Daniela Gorena, and Santiago Blanco for their dedication to the observation protocol. We extend our appreciation to the faculty of Unidad Educativa Sariri, specifically Ezequiel Montiel Espejo, Magda Mamani Condori, and Antonio Mamani Nina, for their collaboration. Furthermore, we acknowledge the technical support and implementation team, Víctor Mamani, Mariela Castel, Naira Mercado, Irene Portocarrero, Madelein Gómez, Ronal Huanca and Damián Villegas, for their outstanding logistical support and assistance in organizing the event. Finally, we thank the students and families who participated in this study."

funding_real = "Funding: This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. The study was conducted using the institutional resources and in-kind support of the authors' affiliated organizations."

conflict = "The authors declare no conflict of interest. The corresponding author is not affiliated with the editorial board of the target journal."

data_avail = "The anonymised dataset, the Python analysis code reproducing all tables and figures, the survey instrument, the observation protocol, the fidelity checklist, the AI safety protocol, and the artifact rubrics are publicly available in the project repository: https://github.com/12ak40/biopochito-sariri-paper."

ai_declaration = "During the preparation of this work, the author(s) used an English language editing, and manuscript formatting. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article. The Biopochito system itself is the subject of the study and was not used to draft this manuscript."

author_contrib = "Author Contributions: Conceptualization, M.A.C.Z.; methodology, M.A.C.Z., Y.A.S., J.G.P.C., and M.L.O.S.; software, M.A.C.Z.; validation, M.A.C.Z., Y.A.S., M.L.O.S., J.E.G.B., J.G.P.C., C.A.C.G., and M.S.; formal analysis, M.A.C.Z.; investigation, Y.A.S.; data curation, M.A.C.Z., G.A.J.A., and P.B.C.; writing—original draft preparation, M.A.C.Z.; writing—review and editing, all authors; supervision, M.A.C.Z. and Y.A.S.; project administration, M.A.C.Z. All authors have read and agreed to the published version of the manuscript."

title = "Biopochito: A Culturally Adapted Science Popularization Platform for Environmental Education and Green Media Literacy"

# --- 2. GENERAR TITLE PAGE ---
doc_title = Document()
doc_title.add_heading('Title Page', 0)
doc_title.add_heading(title, level=1)
doc_title.add_paragraph(autores)
for a in afiliaciones:
    doc_title.add_paragraph(a)
doc_title.add_paragraph(correspondencia)

doc_title.add_heading('Acknowledgements', level=2)
doc_title.add_paragraph(acknowledgements)

doc_title.add_heading('Funding', level=2)
doc_title.add_paragraph(funding_real)

doc_title.add_heading('Conflict of Interest', level=2)
doc_title.add_paragraph(conflict)

doc_title.add_heading('Declaration of Generative AI Use', level=2)
doc_title.add_paragraph(ai_declaration)

doc_title.add_heading('Author Contributions', level=2)
doc_title.add_paragraph(author_contrib)

doc_title.add_heading('Data Availability', level=2)
doc_title.add_paragraph(data_avail)

doc_title.save("05_manuscript/Title_Page.docx")
print("1/4 Title_Page.docx generado.")

# --- 3. GENERAR MANUSCRIPT ANONYMISED ---
doc_anon = Document("05_manuscript/Paper.docx")

# Función para reemplazar texto
def reemplazar(doc, buscar, reemplazar_con):
    for p in doc.paragraphs:
        if buscar in p.text:
            p.text = p.text.replace(buscar, reemplazar_con)

# Borrar autores
reemplazar(doc_anon, "Marco A. Cabero Z.,1,4,5 Yelka Aguilera S.", "Authors blinded for review.")
# Borrar afiliaciones (reemplazar el bloque)
for p in doc_anon.paragraphs:
    if "Andean Road Countries" in p.text and "Beijing" in p.text:
        p.text = "Affiliations blinded for review."
    elif "Unidad Central del Valle del Cauca (UCEVA)" in p.text and "Tuluá" in p.text:
        p.text = ""
    elif "Universidad Privada del Valle" in p.text and "La Paz" in p.text:
        p.text = ""
    elif "Science Culture Construction Research Institute" in p.text:
        p.text = ""
    elif "Journal of Latin American Sciences and Culture, Bolivia" in p.text:
        p.text = ""
    elif "Correspondence: marco.cabero@arcst.org" in p.text:
        p.text = "Correspondence: blinded for review."
    elif "https://github.com/12ak40/biopochito-sariri-paper" in p.text:
        p.text = p.text.replace("https://github.com/12ak40/biopochito-sariri-paper", "[URL blinded for review]")
    elif "The authors express their deepest gratitude" in p.text:
        p.text = "Acknowledgements blinded for review."
    elif "Funding: This research did not receive" in p.text:
        p.text = "Funding: Blinded for review."
    elif "Conceptualization, M.A.C.Z." in p.text:
        p.text = "Author Contributions blinded for review."

doc_anon.save("05_manuscript/Manuscript_Anonymised.docx")
print("2/4 Manuscript_Anonymised.docx generado.")

# --- 4. GENERAR HIGHLIGHTS ---
highlights = """- Offline RAG AI supported a culturally adapted Green MIL workshop.
- Fifty-two children completed paired pre/post assessments.
- Knowledge, attitudes, and curiosity improved after the workshop.
- AI-specific effects could not be isolated from the full intervention.
- Public code and anonymised data support reproducibility."""

with open("05_manuscript/Highlights.txt", "w", encoding="utf-8") as f:
    f.write(highlights)
print("3/4 Highlights.txt generado.")

# --- 5. GENERAR COVER LETTER ---
cover_letter = f"""[Date]

Editor-in-Chief
Computers and Education: Artificial Intelligence (CAEAI)

Dear Editor,

We are pleased to submit our manuscript entitled "{title}" for consideration for publication in Computers and Education: Artificial Intelligence.

This study presents a culturally adapted implementation of an internet-connected, compact AI companion (Biopochito) and a Green Media and Information Literacy (MIL) workshop for children in a high-altitude context in La Paz, Bolivia. To our knowledge, this is one of the first documented implementations of a locally grounded RAG architecture for child-oriented environmental education in Latin America.

Our manuscript makes the following contributions:
1. Technical: Documents a reproducible RAG architecture for resource-constrained environments.
2. Pedagogical: Integrates the UNESCO Green MIL framework with local ecological knowledge (Lake Titicaca).
3. Empirical: Provides quantitative and qualitative evidence of short-term changes in knowledge, attitudes, and curiosity among 52 children.
4. Ethical: Outlines a transparent safety and data-minimisation protocol for AI use with minors.

We have deposited all anonymised data, Python analysis scripts, survey instruments, and rubrics in a public repository (URL blinded in manuscript, available at: https://github.com/12ak40/biopochito-sariri-paper) to ensure full reproducibility and transparency, aligning with CAEAI's open science principles.

As the corresponding author is affiliated with an institution in a lower-middle-income country (Bolivia/Colombia), we kindly request a waiver or discount for the Article Processing Charge (APC) in accordance with Elsevier's waiver policy for authors from developing countries.

We confirm that this manuscript is original, has not been published elsewhere, and is not under consideration by another journal. All authors have approved the manuscript and agree with its submission to CAEAI. We declare no conflicts of interest.

Thank you for considering our work.

Sincerely,

Marco A. Cabero Z.
On behalf of all authors
Andean Road Countries for Science and Technology (ARCST)
Email: marco.cabero@arcst.org
"""

with open("05_manuscript/Cover_Letter.txt", "w", encoding="utf-8") as f:
    f.write(cover_letter)
print("4/4 Cover_Letter.txt generado.")

print("\n¡Todos los archivos de envío han sido generados con éxito en 05_manuscript/!")
