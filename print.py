import streamlit as st
import subprocess

def abrir_calculadora():
    st.title("Abrir Calculadora do Windows")

    if st.button("Abrir Calculadora"):
        try:
            subprocess.run(["C:\Windows\System32\calc.exe"])  # Comando para abrir la calculadora de Windows
        except Exception as e:
            st.error(f"Não foi possível abrir a calculadora: {e}")

if __name__ == "__main__":
    abrir_calculadora()
