import streamlit as st
import importlib
st.title('All Steps Overview')
st.markdown('---')
modules = [
    'pages.1_backend_technologies',
    'pages.2_frontend_technologies',
    'pages.3_database_technologies',
    'pages.4_cloud_technologies',
    'pages.5_hybrid_technologies',
    'pages.6_category_technologies'
]
for mod in modules:
    # This makes the header look clean (e.g., "1 Backend Technologies")
    st.header(mod.split('.')[-1].replace('_',' ').title())
    
    with st.expander(f"Details for {mod}", expanded=True):
        try:
            # Re-import to ensure fresh load if needed
            module = importlib.import_module(mod)
            # If your sub-pages have a 'main()' function, you can call it here:
            # if hasattr(module, 'main'):
            #     module.main()
        except Exception as e:
            st.error(f"Failed to load {mod}: {e}")
            
    st.markdown('---')
    
    
    
