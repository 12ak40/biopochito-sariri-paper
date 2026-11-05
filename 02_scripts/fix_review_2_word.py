from docx import Document
import os

doc_path = "05_manuscript/Paper.docx"
if not os.path.exists(doc_path):
    print(f"ERROR: No se encuentra {doc_path}.")
    exit()

doc = Document(doc_path)

# 1. Reframing the Title (Point 2.1)
doc.paragraphs[0].text = "Biopochito: An Exploratory Implementation of a Culturally Adapted AI-Supported Science Workshop for Green Media Literacy"

# 2. Fix Participant Flow (Point 2.2)
for p in doc.paragraphs:
    if "Fifty-three students enrolled in the activity." in p.text:
        p.text = ("Fifty-four students enrolled in the activity across two days. Of these, two students were excluded from the final analysis (one due to absent post-test data, and one due to missing age-group data), resulting in a final analytical sample of 52 students. "
                  "The intervention was specifically designed to accommodate three distinct age groups: Group 1 (ages 8–10, n=14), Group 2 (ages 11–14, n=18), and Group 3 (ages 15–17, n=20). "
                  "All groups participated in the same three-station workshop, but facilitators adapted the complexity of the AI interactions and the depth of the creative activities according to the age group. Written informed consent was obtained from parents/guardians, with oral assent from the children.")
    
    # 3. Update Ethics Section (Point 2.3)
    elif "This study was conducted in accordance with the ethical principles of the Declaration of Helsinki" in p.text:
        p.text = ("This study was conducted in accordance with the ethical principles of the Declaration of Helsinki and the Bolivian Code of Health (Código de Salud, Ley 3131) regarding research with human participants. "
                  "Because the authors' institutions (ARCST and UCEVA) do not have a formally constituted ethics committee with jurisdiction over international school-based research, and no independent committee was available within the project timeline, a formal ethics review was not obtained. "
                  "To mitigate this limitation, the authors implemented rigorous safeguards: (1) The school principal provided written institutional authorization; (2) Written informed consent was obtained from all parents/guardians, and oral assent was obtained from children, who were explicitly told they could decline any activity or withdraw at any time without consequence; (3) Teachers were present during assent to manage power dynamics; (4) No personal data, names, or audio were stored on the AI tablets; (5) All video recordings were temporarily stored on a password-protected device, transcribed, and deleted immediately after anonymization. "
                  "The public repository contains only de-identified, aggregated data, and the risk of re-identification is minimal. Explicit parental permission was obtained to publish anonymized, translated quotes from the children's videos.")

    # 4. Reframing the AI contribution (Point 2.1)
    elif "This study provides preliminary evidence of positive short-term changes following participation in a culturally adapted Green MIL workshop." in p.text:
        p.text = ("This study provides preliminary evidence of positive short-term changes following participation in a multi-component, Biopochito-supported Green MIL workshop. The design does not permit isolating the specific causal effect of the AI component from the broader educational context (which included art, video production, and family co-creation). The changes may have been influenced by the novelty of the activity, the participation of families, or the pre-test/post-test design itself. Therefore, this study is framed as an exploratory implementation and feasibility study, estimating change after participation in the combined workshop rather than the isolated effect of AI.")

    # 5. Remove "Low-energy" claim (Point 2.6)
    elif "low-energy AI companions" in p.text:
        p.text = p.text.replace("low-energy AI companions", "locally hosted, offline AI companions")

    # 6. Fix Reliability claim in 2.5 (Point 2.7)
    elif "pilot test confirmed the clarity of the items and the internal consistency" in p.text:
        p.text = ("The pilot test confirmed the clarity of the items and the feasibility of the instrument. Because formal reliability assessment (e.g., Cronbach's alpha) was not feasible due to the exploratory nature of the study and the small sample size, no claims of internal consistency reliability or construct validity are made. The full Spanish instrument and scoring key are provided in the public repository for transparency.")

    # 7. Clarify Knowledge scoring (Point 2.8)
    elif "Section D (Knowledge): 4 multiple-choice + 4 open-ended items. Range: 0–16." in p.text:
        p.text = ("Section D (Knowledge): 8 items. Items D1-D4 were multiple-choice (scored 0 for incorrect, 1 for correct). Items D5-D8 were open-ended and scored using a 0-2 rubric (0=incorrect/no response, 1=partial, 2=complete), yielding a total range of 0-12. Scoring was conducted by two independent evaluators; disagreements were resolved by consensus. The full scoring rubric is provided in Appendix A.")

doc.save("05_manuscript/Paper_STRUCTURAL_FIXES.docx")
print("¡Éxito! Documento guardado como 05_manuscript/Paper_STRUCTURAL_FIXES.docx")
