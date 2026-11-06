from docx import Document
import re

doc = Document("05_manuscript/Paper.docx")

# 1. Anonimizar párrafos (Autores, Agradecimientos, GitHub, Colegio)
for p in doc.paragraphs:
    if "Marco A. Cabero Z." in p.text or "José Gabriel Pérez" in p.text:
        p.text = "Author names blinded for review."
    elif "Correspondence:" in p.text:
        p.text = "Correspondence: blinded for review."
    elif "https://github.com/12ak40/biopochito-sariri-paper" in p.text:
        p.text = p.text.replace("https://github.com/12ak40/biopochito-sariri-paper", "[URL blinded for review]")
    elif "Unidad Educativa Sariri" in p.text:
        p.text = p.text.replace("Unidad Educativa Sariri", "a participating school in La Paz, Bolivia")
    elif "The authors thank the students, families, and educators" in p.text:
        p.text = "Acknowledgements blinded for review."

# 2. Borrar el título original y reemplazarlo (por si acaso)
doc.paragraphs[0].text = "Biopochito: An Exploratory Implementation of a Culturally Adapted AI-Supported Science Workshop for Green Media Literacy"

doc.save("05_manuscript/Manuscript_Anonymised.docx")
print("¡Éxito! Manuscript_Anonymised.docx creado (listo para revisores).")
