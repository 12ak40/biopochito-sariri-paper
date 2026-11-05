from docx import Document
import os

doc_path = "05_manuscript/Paper.docx"
if not os.path.exists(doc_path):
    print(f"ERROR: No se encuentra {doc_path}.")
    exit()

doc = Document(doc_path)

# --- 4.1 y 4.2: Nueva sección de contribuciones al final de la Introducción ---
contrib_text = (
    "\n\n1.4 Specific Contributions of this Study\n"
    "To clarify the novelty of this work beyond the combination of existing elements, we articulate our contributions as follows: "
    "(1) Technical: We document an offline Retrieval-Augmented Generation (RAG) architecture (Biopochito) designed specifically for child-oriented science education without internet access. "
    "(2) Pedagogical: We present a Green MIL design aimed at environmental misinformation and verification. "
    "(3) Empirical: We provide a feasibility and implementation study in a Latin American school, detailing short-term changes. "
    "(4) Cultural: We describe a culturally adapted interaction model grounded in local ecological knowledge. "
    "(5) Ethical: We outline a reproducible safety and data-minimisation protocol for AI use with minors. "
    "We do not present this prototype as a validated educational technology, but as an exploratory implementation. "
    "Regarding cultural adaptation, the local knowledge (e.g., Lake Titicaca biodiversity, totora reeds) was selected through consultation with local educators at Unidad Educativa Sariri. "
    "These educators validated the accuracy and age-appropriateness of the content, ensuring respectful representation. No Indigenous community knowledge was used without explicit educational contextualization, and the database is treated as educational content rather than proprietary data."
)

# --- 4.3: Mapeo de competencias MIL en Métodos ---
mil_mapping_text = (
    "\n\nTo ensure construct validity for our Green MIL outcomes, we mapped each claimed competency to observable behaviors: "
    "(a) Curiosity was measured by the pre/post survey and coded from open-ended questions; "
    "(b) Verification (MIL) was mapped to items asking 'How do we know?', scored on the E1 rubric; "
    "(c) Responsible Communication was mapped to the Station C video rubric criteria (Evidence, Empathy, Call to Action). "
    "Environmental advocacy statements were not treated as source verification, but as a separate outcome of responsible communication."
)

for p in doc.paragraphs:
    # Insertar 1.4 al final de la Introducción
    if "What qualitative evidence of engagement, critical questioning, and MIL competencies emerged" in p.text:
        p.text = p.text + contrib_text
    
    # Insertar mapeo MIL en Métodos (después del párrafo de la rúbrica)
    elif "This dual approach allowed for methodological triangulation" in p.text:
        p.text = p.text + mil_mapping_text

# --- 6.3, 6.5, 7: Declaraciones obligatorias al final (Elsevier) ---
# Encontramos el final del documento (Conflict of Interest)
for p in doc.paragraphs:
    if "The authors declare no conflict of interest" in p.text:
        p.text = p.text + (
            "\n\nFunding Statement: This research received no specific grant from public, commercial, or not-for-profit funding agencies. "
            "In-kind support (tablets, platform development, and staff time) was provided by the Andean Road Countries for Science and Technology (ARCST) and the Unidad Central del Valle del Cauca (UCEVA). "
            "\n\nDeclaration of Generative AI and AI-assisted technologies in the writing process: During the preparation of this work, the author(s) used ChatGPT (OpenAI) to assist with statistical code verification, English language editing, and manuscript formatting. "
            "After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article. The Biopochito system itself is the subject of the study and was not used to draft this manuscript. "
            "\n\nAuthor Contributions: Conceptualization, M.A.C.Z.; methodology, M.A.C.Z. and J.G.P.C.; software, M.A.C.Z.; validation, M.L.O.S. and C.A.C.G.; formal analysis, M.A.C.Z.; investigation, Y.A.S.; data curation, M.A.C.Z.; writing—original draft preparation, M.A.C.Z.; writing—review and editing, all authors. All authors have read and agreed to the published version of the manuscript."
        )

doc.save("05_manuscript/Paper_CAEAI_READY.docx")
print("¡Éxito! Documento guardado como 05_manuscript/Paper_CAEAI_READY.docx")
