import streamlit as st
import math

def calcular_area(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro(radio):
    return 2 * math.pi * radio

def main():
    st.title("calculo del area y perimetro de una circunferencia:")

    radio = sr.number_input("ingrese el radio de la circunferencia:", min_value=0.0, step=0)

    if radio > 0:
        area = calcular_area(radio)
        perimetro = calcular_perimetro(radio)

        st.write(f"area: {area:.2f}")
        st.write(f"perimetro: {perimetro:.2f}") 
    else:
        st.write("por favor, ingrese un radio mayor a cero.")

if __name__ =="__main__"
main()                       