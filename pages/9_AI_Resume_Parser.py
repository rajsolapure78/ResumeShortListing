
# 9_AI_Resume_Parser.py
import streamlit as st
import spacy, re, json
from PyPDF2 import PdfReader
from docx import Document

st.title("🧠 Step 9: AI Resume Parser & Auto Match")

try:
    nlp = spacy.load("en_core_web_sm")
except Exception:
    nlp = None

if "uploaded_file" not in st.session_state:
    st.warning("Please upload your resume first.")
else:
    uploaded_file = st.session_state["uploaded_file"]
    file_type = uploaded_file.name.split(".")[-1].lower()

    resume_text = ""
    if file_type == "pdf":
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            resume_text += page.extract_text() or ""
    elif file_type == "docx":
        doc = Document(uploaded_file)
        for para in doc.paragraphs:
            resume_text += para.text + "\\n"

    resume_text = re.sub(r"[^A-Za-z0-9+]+", " ", resume_text)
    detected = set()
    if nlp is not None:
        doc = nlp(resume_text)
        tokens = [t.text.lower() for t in doc if not t.is_stop and not t.is_punct]
        tech_terms = [
            "python","java","javascript","node","react","angular","vue","django","flask",
            "aws","azure","gcp","docker","kubernetes","mysql","mongodb","postgresql",
            "flutter","react native","ionic","xamarin","devops","terraform","linux"
        ]
        detected = {t for t in tech_terms if t in " ".join(tokens)}
    st.markdown("### 🤖 Extracted Skills from Resume")
    st.info(", ".join(sorted(detected)) or "None found")

    selected = [s.lower() for key in ["backend","frontend","database","cloud","hybrid","category"]
                for s in st.session_state.get(f"selected_{key}", [])]

    matched = [s for s in selected if s in detected]
    missing = [s for s in selected if s not in detected]
    score = round((len(matched) / len(selected)) * 100, 2) if selected else 0

    st.markdown("## 🎯 AI Match Result")
    st.metric("AI Match Percentage", f"{score}%")

    st.markdown("### ✅ Matched Skills")
    st.success(", ".join(matched) if matched else "No matches found.")

    st.markdown("### ❌ Missing Skills")
    st.error(", ".join(missing) if missing else "All matched!")

    if st.button("💾 Export AI Match Report"):
        report = {"ai_detected_skills": sorted(list(detected)), "selected_skills": selected, "matched": matched, "missing": missing, "match_score": score}
        with open("ai_resume_match_report.json", "w") as f:
            json.dump(report, f, indent=4)
        st.success("✅ Exported as ai_resume_match_report.json")
