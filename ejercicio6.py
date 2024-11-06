import streamlit as st
import random

def crear_array_streamlit(tamano):
    array = [random.randint(0, 9) for _ in range(tamano)]
    return array

def calcular_media(array):
    if len(array) == 0:
        return 0
    return sum(array) / len(array)

# Ejecución del programa en Streamlit
def main():
    st.title("Ejercicio 8: Media de Valores en un Array")

    # Seleccionar tamaño del array y rellenar el array
    tamano = st.number_input("Ingrese el tamaño del array:", min_value=1, step=1)

    if tamano > 0:
        # Rellenar el array con números aleatorios entre 0 y 9
        array = crear_array_streamlit(tamano)
        media = calcular_media(array)
        
        # Mostrar el array y la media
        st.write("Array generado:", array)
        st.write(f"La media de los valores en el array es: {media:.2f}")

if __name__ == "__main__":
    main()
