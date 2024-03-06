import streamlit as st

def calculadora():
    st.title("Calculadora Simples")

    num1 = st.number_input("Digite o primeiro número", step=1)
    operacion = st.selectbox("Qual a operação?", ["Soma", "Subtração", "Multiplicação", "Divisão"])
    num2 = st.number_input("Digite o segundo número", step=1)

    if st.button("Calcular"):
        resultado = realizar_calculo(num1, num2, operacion)
        st.success(f"O resultado de {num1} {operacion} {num2} é: {resultado}")

def realizar_calculo(num1, num2, operacion):
    if operacion == "Soma":
        return num1 + num2
    elif operacion == "Subtração":
        return num1 - num2
    elif operacion == "Multiplicação":
        return num1 * num2
    elif operacion == "Divisão":
        if num2 != 0:
            return num1 / num2
        else:
            st.error("¡Erro! Não se pode dividir por zero.")
            return None

if __name__ == "__main__":
    calculadora()
