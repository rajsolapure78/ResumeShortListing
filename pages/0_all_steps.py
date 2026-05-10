import streamlit as st
import importlib
st.title('All Steps Overview')
st.markdown('---')
modules = ['resume_shortlisting_app.pages.1_backend_technologies', 'resume_shortlisting_app.pages.2_frontend_technologies', 'resume_shortlisting_app.pages.3_database_technologies', 'resume_shortlisting_app.pages.4_cloud_technologies', 'resume_shortlisting_app.pages.5_hybrid_technologies', 'resume_shortlisting_app.pages.6_category_technologies']
for mod in modules:
    st.header(mod.split('.')[-1].replace('_',' ').title())
    with st.expander(mod, expanded=True):
        try:
            importlib.import_module(mod)
        except Exception as e:
            st.error(f"Failed to load {mod}: {e}")
    st.markdown('---')
