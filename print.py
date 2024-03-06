import streamlit as st

def menu():
    st.title("Menu com 3 Botões")

    # Botões no menu
    opcao = st.sidebar.radio("Selecione uma opção:", ["Botão 1", "Botão 2", "Botão 3"])

    # Conteúdo conforme a opção selecionada
    if opcao == "Botão 1":
        st.header("Conteúdo do Botão 1")
        st.write("Este é o conteúdo do Botão 1.")
    elif opcao == "Botão 2":
        st.header("Conteúdo do Botão 2")
        st.write("Este é o conteúdo do Botão 2.")
    elif opcao == "Botão 3":
        st.header("Conteúdo do Botão 3")
        st.write("Este é o conteúdo do Botão 3.")

if __name__ == "__main__":
    menu()
