import streamlit as st
import subprocess

def abrir_calculadora():
    st.title("Abrir Calculadora de Windows")

    if st.button("Abrir Calculadora"):
        try:
            subprocess.run(["calc.exe"])  # Comando para abrir la calculadora de Windows
        except Exception as e:
            st.error(f"Error al abrir la calculadora: {e}")

if __name__ == "__main__":
    abrir_calculadora()
