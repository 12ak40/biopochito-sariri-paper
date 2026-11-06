from docx import Document

# Datos actualizados con letras minúsculas y direcciones completas
autores = (
    "Marco A. Cabero Z.ª,ᵈ,ᵉ, Yelka Aguilera S.ª,ᶜ,ᵈ,ᵉ, José G. Pérez C.ᵇ,ᵈ,ᵉ, "
    "Mary L. Ojeda S.ᵇ,ᵈ,ᵉ, Jorge E. Guevara B.ª,ᵇ,ᵈ, Moiya Sullivanª,ᵈ,ᵉ, "
    "Gabriel A. Jimenez A.ª,ᵈ,ᵉ, Pablo Baldiviezo C.ª,ᵈ,ᵉ, Christian A. Cuero G.ª,ᵇ,ᵈ"
)

# Nota: Usamos caracteres Unicode de superíndice para que se vean como letras pequeñas en el Word.
afiliaciones = [
    "ª Andean Road Countries for Science and Technology (ARCST), Beijing, China",
    "ᵇ Unidad Central del Valle del Cauca (UCEVA), Tuluá, Valle del Cauca, Colombia",
    "ᶜ Universidad Privada del Valle, La Paz, Bolivia",
    "ᵈ Science Culture Construction Research Institute, Cochabamba, Bolivia",
    "ᵉ Journal of Latin American Sciences and Culture, Bolivia"
]

correspondencia = "Correspondence to: Marco A. Cabero Z., Andean Road Countries for Science and Technology (ARCST), Beijing, China. Email: marco.cabero@arcst.org"

acknowledgements = (
    "The authors express their deepest gratitude to Cecilia E. Pinedo, Director of Unidad Educativa Sariri, for her invaluable institutional support. "
    "We also thank the observation protocol team: Santiago Blanco, Daniela Gorena, and Marco Antonio Viera. "
    "We extend our appreciation to the faculty of Unidad Educativa Sariri: Magda Mamani Condori, Antonio Mamani Nina, and Ezequiel Montiel Espejo, for their collaboration. "
    "Furthermore, we acknowledge the technical support and implementation team: Mariela Castel, Madelein Gómez, Ronal Huanca, Naira Mercado, Irene Portocarrero, and Damián Villegas, for their outstanding logistical support. "
    "Finally, we thank the students and families who participated in this study."
)

competing_interests = "The authors declare no competing financial interests or personal relationships that could have appeared to influence the work reported in this paper."

title = "Biopochito: A Culturally Adapted Science Popularization Platform for Environmental Education and Green Media Literacy"

# Generar el documento
doc = Document()
doc.add_heading('Title Page', 0)
doc.add_heading(title, level=1)

doc.add_paragraph(autores)
for a in afiliaciones:
    doc.add_paragraph(a)

doc.add_paragraph(correspondencia)

doc.add_heading('Acknowledgements', level=2)
doc.add_paragraph(acknowledgements)

doc.add_heading('Declaration of Competing Interests', level=2)
doc.add_paragraph(competing_interests)

doc.save("05_manuscript/Title_Page.docx")
print("¡Title_Page.docx actualizado con el formato exacto de Elsevier!")
