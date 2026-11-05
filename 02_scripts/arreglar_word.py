from docx import Document
import os

# Ahora busca en la raíz del proyecto
doc_path = "Paper.docx"

if not os.path.exists(doc_path):
    print(f"ERROR: No se encuentra {doc_path} en la carpeta principal.")
    exit()

doc = Document(doc_path)

reemplazos = {
    # Abstract y Texto (r corregidos)
    "Knowledge (p < 0.0001, r = 0.69), Environmental Attitude (p = 0.0053, r = 0.40), and Curiosity (p = 0.0077, r = 0.38)": 
    "Knowledge (p < 0.0001, r = 0.78), Environmental Attitude (p = 0.0053, r = 0.52), and Curiosity (p = 0.0077, r = 0.48)",
    
    "did not remain statistically significant after correction (p = 0.0477, r = 0.28)": 
    "did not remain statistically significant after correction (p = 0.0477, r = 0.33)",
    
    # Sección 4.1 (r corregidos)
    "improvement in Knowledge (p < 0.0001, r = 0.69)": 
    "improvement in Knowledge (p < 0.0001, r = 0.78)",
    
    "MIL Self-Efficacy (p = 0.0477, r = 0.28)": 
    "MIL Self-Efficacy (p = 0.0477, r = 0.33)",

    # Sección 3.3 (Estación B y C)
    "A total of 25 student artifacts were evaluated": 
    "A total of 30 student artifacts were evaluated",
    "The overall average score was 2.80 out of 4.0": 
    "The overall average score was 2.87 out of 4.0",
    "Five group audio-visual productions were evaluated": 
    "Three group audio-visual productions were evaluated",
    "Notable quotes included: \"Caring for the environment is not an option, it is an obligation\" and \"Do not pollute Lake Titicaca.\"":
    "Notable quotes included: \"Caring for the environment is not an option, it is an obligation\", \"Do not forget to take care of the environment\", and \"Do not pollute Lake Titicaca.\"",
    
    # Sección 2.2 (Datos de los grupos de edad)
    "Group 1 (ages 8–10, n=[XX]), Group 2 (ages 11–14, n=[YY]), and Group 3 (ages 15–17, n=[ZZ])":
    "Group 1 (ages 8–10, n=14), Group 2 (ages 11–14, n=18), and Group 3 (ages 15–17, n=20)"
}

for p in doc.paragraphs:
    for viejo, nuevo in reemplazos.items():
        if viejo in p.text:
            p.text = p.text.replace(viejo, nuevo)

# Tabla 1
for table in doc.tables:
    if len(table.columns) == 7 and "Wilcoxon W" in table.rows[0].cells[4].text:
        table.rows[1].cells[6].text = "0.78 (large)"
        table.rows[2].cells[3].text = "+2.38"
        table.rows[2].cells[6].text = "0.52 (large)"
        table.rows[3].cells[6].text = "0.48 (moderate-to-large)"
        table.rows[4].cells[3].text = "+1.27"
        table.rows[4].cells[6].text = "0.33 (moderate)"
        print("Tabla 1 actualizada correctamente.")

# Tabla 2
for table in doc.tables:
    if len(table.columns) == 4 and "Example Quote" in table.rows[0].cells[1].text:
        table.rows[2].cells[2].text = "43"
        table.rows[2].cells[3].text = "82.7%"
        table.rows[3].cells[2].text = "17"
        table.rows[3].cells[3].text = "32.7%"
        table.rows[4].cells[2].text = "22"
        table.rows[4].cells[3].text = "42.3%"
        print("Tabla 2 actualizada correctamente.")

doc.save("Paper_CORREGIDO.docx")
print("¡Éxito! Archivo guardado como Paper_CORREGIDO.docx en la carpeta principal.")
