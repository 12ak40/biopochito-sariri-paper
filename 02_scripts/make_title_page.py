from docx import Document

doc = Document()
doc.add_heading('Title Page', 0)

doc.add_heading('Biopochito: An Exploratory Implementation of a Culturally Adapted AI-Supported Science Workshop for Green Media Literacy', level=1)

doc.add_paragraph('Marco A. Cabero Z.¹, José Gabriel Pérez Canencio², Mary Luz Ojeda Solarte², Christian Andrés Cuero Gamboa², Jorge Enrique Guevara Bejarano², Yelka Aguilera Santos³')
doc.add_paragraph('¹ Andean Road Countries for Science and Technology (ARCST), Beijing, China')
doc.add_paragraph('² Unidad Central del Valle del Cauca (UCEVA), Tuluá, Colombia')
doc.add_paragraph('³ Independent Researcher, La Paz, Bolivia')
doc.add_paragraph('Correspondence: marco.cabero@arcst.org')

doc.add_heading('Acknowledgements', level=2)
doc.add_paragraph('The authors thank the students, families, and educators of Unidad Educativa Sariri for their participation. We also thank the Andean Road Countries for Science and Technology (ARCST), UCEVA, IGSCLAC, and JLASC for their institutional and technical support.')

doc.add_heading('Funding', level=2)
doc.add_paragraph('This research received no specific grant from public, commercial, or not-for-profit funding agencies. In-kind support (tablets, platform development, and staff time) was provided by the Andean Road Countries for Science and Technology (ARCST) and the Unidad Central del Valle del Cauca (UCEVA).')

doc.add_heading('Conflict of Interest', level=2)
doc.add_paragraph('The authors declare no conflict of interest. The corresponding author is not affiliated with the editorial board of the target journal.')

doc.add_heading('Data Availability', level=2)
doc.add_paragraph('The anonymised dataset, the Python analysis code reproducing all tables and figures, the survey instrument, the observation protocol, the fidelity checklist, the AI safety protocol, and the artifact rubrics are publicly available in the project repository: https://github.com/12ak40/biopochito-sariri-paper')

doc.add_heading('Declaration of Generative AI Use', level=2)
doc.add_paragraph('During the preparation of this work, the author(s) used ChatGPT (OpenAI) to assist with statistical code verification, English language editing, and manuscript formatting. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article. The Biopochito system itself is the subject of the study and was not used to draft this manuscript.')

doc.save("05_manuscript/Title_Page.docx")
print("¡Éxito! Title_Page.docx creado.")
