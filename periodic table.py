import streamlit as st
import math

st.set_page_config(page_title="Kalkulator pH & pOH", layout="centered")

# Title
st.title("⚗️ Games Kimia")

# Description
st.write("""
Aplikasi ini berguna untuk mempelajari tabel periodic unsur""")

# Apply dark mode
if show_dark_mode:
    st.markdown(
        """
        <style>
            body { background-color: #1e1e1e; color: white; }
            .stApp { background-color: #1e1e1e; }
        </style>
        """, unsafe_allow_html=True
    )
