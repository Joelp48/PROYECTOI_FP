import streamlit as st

#titulo a la aplicacion
st.title("Introduccion a variables y tipos de datos Python")

#descripcion inicial
st.write("Python es un lenguaje de programacion donde...")

#sección para varible de tipo entero
st.header("Ejemplo 1: Enteros")
st.write("En python un entero (integer) es un numero sin decimales por ejemplo:")

#Definir una variable entera
int_variable = 42
st.code(f"int_variable = (int_variable) # Tipo: {type(int_variable)}")