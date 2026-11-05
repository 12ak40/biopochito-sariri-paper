from docx import Document
import os

doc_path = "05_manuscript/Paper.docx"
if not os.path.exists(doc_path):
    print(f"ERROR: No se encuentra {doc_path}.")
    exit()

doc = Document(doc_path)

# Textos nuevos
nuevo_2_6 = (
    "Quantitative data were analysed using Python 3.13 (SciPy version 1.13). Because Shapiro–Wilk tests indicated non-normal distributions for the difference scores (p < 0.05 for all), non-parametric tests were prioritized. However, the choice of the Wilcoxon signed-rank test was also justified by the ordinal nature of the Likert-scale items and the small sample size, rather than relying solely on the normality p-value. "
    "The Wilcoxon test was executed using scipy.stats.wilcoxon (default settings: two-sided, zero_method='wilcox', asymptotic ties). The reported W represents the smaller of the positive and negative rank sums, following SciPy's convention. We report the exact W+ and W- sums in Table 1 to avoid ambiguity. Effect sizes were calculated using the signed rank-biserial correlation (r = (W+ - W-) / (W+ + W-)), with positive values indicating an increase from pre- to post-test. To avoid relying on generic heuristic thresholds, the effect sizes are presented with their continuous values and 95% confidence intervals (bootstrap, 2000 resamples) rather than categorical labels. "
    "Multiple Comparisons: A Bonferroni correction was applied to the four pre-specified primary outcomes (Knowledge, Attitude, Curiosity, MIL Self-Efficacy), establishing a threshold of p = 0.0125. The artifact rubric scores and qualitative themes were treated as exploratory descriptive analyses and were not included in this correction family. The analysis was not preregistered."
)

nuevo_3_1 = (
    "The activity was successfully implemented across two sessions. 52 valid pre/post pairs were collected. The fidelity checklist indicated that the core components of the three stations were delivered as planned in both sessions.\n\n"
    "Exploratory Analysis by Age Group: Although the study was not powered to detect subgroup differences, descriptive statistics were examined by age group (Group 1: 8–10y, n=14; Group 2: 11–14y, n=18; Group 3: 15–17y, n=20). All three groups showed positive shifts in medians across most constructs. For Knowledge, the medians increased from 3.0 to 5.0 in Group 1, from 6.5 to 8.0 in Group 2, and from 6.0 to 8.0 in Group 3. Environmental Attitude increased in all groups (G1: 23.0 to 24.0; G2: 20.0 to 21.0; G3: 20.0 to 22.0). Curiosity remained stable in Group 2 (18.5 to 18.5) but increased in Group 1 (23.5 to 24.0) and Group 3 (20.0 to 21.0). MIL Self-Efficacy showed mixed results (G1: 32.0 to 32.5; G2: 28.5 to 27.0; G3: 29.5 to 30.0). Due to developmental heterogeneity and the small sample size per cell, no significance testing was performed on these subgroups. Facilitators adapted the complexity of AI interactions for older groups, which may have influenced the depth of responses."
)

nuevo_3_3 = (
    "3.3 Exploratory Analyses: Artifacts and Qualitative Themes (RQ3)\n"
    "Deductive Rubric Classification: The qualitative themes presented in Table 2 were derived via a deductive classification system based on the post-test rubric scores for items D5, D6, D8, and E1, rather than an inductive thematic analysis. This structured classification ensures reproducibility. Two independent coders applied the rubric, achieving 85% initial agreement (34/40 excerpts) before consensus.\n"
    "Artifact Rubric Analysis: Station B (Stories and Art) artifacts were produced individually by the children. A total of 30 individual artifacts were scored by two facilitators using a 4-point rubric (dimensions: Connection, Creativity, Expression, Detail). Inter-rater reliability was confirmed by consensus scoring. The overall average score was 2.87 out of 4.0. "
    "Station C (Video) artifacts were group productions, resulting in three final videos. Therefore, the unit of analysis for Station C is the group, not the individual child. The three videos were evaluated using a 4-point rubric (dimensions: Evidence, Empathy, Call to Action, MIL), yielding an average score of 3.42 out of 4.0. Because this is based on three group products, it should be interpreted as a descriptive finding of group collaboration rather than a robust estimate of individual performance. The full rubric and evaluator guide are provided in the public repository."
)

for i, p in enumerate(doc.paragraphs):
    # 2.6 Data analysis
    if "Quantitative data were analysed using Python" in p.text:
        p.text = nuevo_2_6
    # 3.1 Implementation
    elif "The activity was successfully implemented across two sessions" in p.text and "52 valid pre/post pairs" in p.text:
        # We need to insert the new paragraph. Python-docx doesn't have an easy "insert" function, 
        # so we append it to the existing paragraph.
        p.text = nuevo_3_1
    # 3.3 Artifacts and Qualitative
    elif "Open-ended questions and thematic analysis" in p.text or "Artifact Rubric Analysis" in p.text:
        # This might span multiple paragraphs, so we replace the first one and clear the others if needed.
        if "Open-ended" in p.text:
            p.text = nuevo_3_3
        elif "Station B" in p.text or "Station C" in p.text:
            p.text = "" # Clear the old text

# Add Limitation
for p in doc.paragraphs:
    if "AI isolation:" in p.text:
        # Append the new limitation right after
        p.text = p.text + "\nArtifact units of analysis: While Station B artifacts were individual, Station C videos were group productions (n=3). The high scores for Station C reflect group dynamics and cannot be generalized to individual student competencies."

doc.save("05_manuscript/Paper_FINAL_REVISION.docx")
print("¡Éxito! Documento guardado como 05_manuscript/Paper_FINAL_REVISION.docx")
