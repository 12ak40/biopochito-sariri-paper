# Appendix E: Biopochito AI Technical Specifications and Safety Audit

## 1. System Architecture
*   **Base Model:** Llama-3-8B-Instruct (Meta AI).
*   **Quantization:** 4-bit quantization via GGUF format (Q4_K_M).
*   **Inference Framework:** llama.cpp running locally on Android tablets (OS: Android 12+).
*   **Hardware:** Generic tablets (8GB RAM, Octa-core processors). No internet access was available during inference.
*   **Retrieval-Augmented Generation (RAG):** Custom rule-based retrieval. The offline database contains approximately 500 text chunks sourced from JLASC publications and local ecological records about Lake Titicaca.
*   **Retrieval Threshold:** Cosine similarity > 0.75. If below this, the model triggers a deferral prompt.
*   **Generation Settings:** Temperature = 0.7, Top-P = 0.9, Max tokens = 150, Context length = 2048.
*   **Language:** Spanish (prompts and generation).

## 2. Prompt Template (System Instructions)
> "Eres Biopochito, un compañero de IA para niños en Bolivia. Tu objetivo es fomentar la curiosidad y el pensamiento crítico sobre el Lago Titicaca. Si el usuario pregunta algo fuera de tu base de datos (la base de datos contiene información sobre la rana Telmatobius culeus, la totora, los peces Orestias y la contaminación del lago), debes responder exactamente: '¡Esa es una gran pregunta! ¿Qué crees que podríamos hacer para averiguarlo?' No inventes datos científicos. Responde de manera sencilla y amigable."

## 3. Safety and Factuality Audit
*   **Total interactions logged:** 342 dialogues across the two days.
*   **Audit sampling:** A random sample of 20% (68 dialogues) was selected using a random number generator.
*   **Auditors:** Two independent research assistants (not involved in facilitation) reviewed the transcripts.
*   **Factuality Rubric:** 
    *   *Accurate:* Information aligns with the offline database.
    *   *Inaccurate:* Contradicts the database or hallucinated facts.
    *   *Deferral:* Successfully triggered the deferral prompt.
    *   *Unsafe:* Inappropriate language or personal data request.
*   **Results:** 
    *   Accurate: 52 (76.5%)
    *   Deferral (Out-of-scope): 12 (17.6%)
    *   Inaccurate (Hallucination): 4 (5.9%). All 4 were minor taxonomic errors (e.g., confusing the size of the frog).
    *   Unsafe: 0 (0%).
*   **Corrective Procedure:** When facilitators observed an inaccurate response in real-time, they intervened to correct the child and reported the error to the technical team for database updates.
