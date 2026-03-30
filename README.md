# 🎓 RAG Quiz Generator 
### **Automated MCQ Generation Pipeline for Academic PDFs**

This repository contains a high-performance **Retrieval-Augmented Generation (RAG)** pipeline designed to transform static university handouts into validated, grounded Multiple Choice Questions (MCQs). This project serves as a functional case study for the **CS403 Database Management Systems** curriculum.

## 🚀 Overview
Traditional manual quiz creation is time-consuming. This system automates the process by extracting text from academic PDFs and using a Large Language Model (LLM) to generate pedagogically sound assessments. To ensure 100% data integrity, the system uses a **dual-layer validation logic** (Pydantic schemas) to eliminate "hallucinations" and structural errors.

## 🛠️ Tech Stack
* **Intelligence Layer:** Gemini 2.5 Flash
* **Data Extraction:** PyMuPDF (`pymupdf`)
* **Structural Validation:** Pydantic (Python Data Validation)
* **Output Format:** Structured CSV / JSON

## ✨ Key Features
* **Contextual Grounding:** Every question is directly retrieved from source handouts, ensuring 1:1 accuracy to the specific syllabus.
* **Pedagogical Explanations:** Generates detailed "Reasoning" fields for every answer to support active recall.
* **Zero-Hallucination Framework:** Uses a "Constraint-First" prompting strategy combined with Pydantic class enforcement.
* **High Efficiency:** Capable of generating a validated batch of 10 complex MCQs in approximately **25 seconds**.

## 📄 Research & Publication
This project is the official implementation for the research paper:  
**"Enhancing Self-Regulated Learning: Evaluating a RAG and LLM-Driven Quiz Generator for Academic PDFs"** *Submitted to the **Journal of Social Sciences and Educational Practices (JSSEP)**.*

## 📂 Repository Structure
* [main.py](main.py) - Core RAG pipeline and Pydantic logic.
* `requirements.txt` - Project dependencies.
* `results_sample.csv` - Sample of generated validated output.
* `README.md` - Project documentation.

## ⚙️ Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/rag-quiz-generator.git](https://github.com/yourusername/rag-quiz-generator.git)
