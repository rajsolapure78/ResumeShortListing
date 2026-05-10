
# app.py - launcher (a simple landing that lets Streamlit detect pages)
import streamlit as st
st.set_page_config(page_title="Resume Shortlisting App", page_icon="🧾")
st.title("Resume Shortlisting App")
st.markdown("""
Welcome — use the sidebar to navigate between steps.
- Home: Upload resume
- Backend..Categories: Edit/select tech lists
- Summary: View & export selections
- Smart Shortlisting / AI Parser: Match %
- Batch Ranking: Upload multiple resumes & export CSV
- All Steps: View all sections on one page
""")
