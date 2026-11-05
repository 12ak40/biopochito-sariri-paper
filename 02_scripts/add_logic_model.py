from docx import Document
import os

doc_path = "05_manuscript/Paper.docx"
if not os.path.exists(doc_path):
    print(f"ERROR: No se encuentra {doc_path}.")
    exit()

doc = Document(doc_path)

logic_model_text = (
    "\n\nLogic Model: The intervention is a multi-component educational package. "
    "We hypothesize that Station A (AI dialogue) primarily supports Knowledge and Curiosity by providing immediate, interactive answers. "
    "Station B (Stories and Art) primarily supports Environmental Attitude by fostering emotional connection. "
    "Station C (Video) primarily supports MIL Self-Efficacy and Responsible Communication through group co-creation. "
    "The pre/post survey measures the combined effect of these components. However, this exploratory study does not isolate the specific contribution of each station."
)

for p in doc.paragraphs:
    if "A mixed-methods, exploratory case study design was employed" in p.text:
        # Añadimos el Logic Model al final del párrafo de Study Design
        p.text = p.text + logic_model_text
        print("Logic Model insertado en la Sección 2.1.")
        break

doc.save("05_manuscript/Paper_with_logic_model.docx")
print("¡Éxito! Archivo guardado como 05_manuscript/Paper_with_logic_model.docx")
