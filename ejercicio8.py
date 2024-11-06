import streamlit as st

def crear_array():
    array = list(range(1, 101))
    return array

def calcular_suma(array):
    return sum(array)

def calcular_media(array):
    if len(array) == 0:
        return 0
    return sum(array) / len(array)

# Ejecución del programa en Streamlit
def main():
    st.title("Ejercicio 10: Suma y Media de un Array de 100 Números")

    # Crear el array de números del 1 al 100
    array = crear_array()
    suma = calcular_suma(array)
    media = calcular_media(array)

    # Mostrar el array, la suma y la media
    st.write("Array de 100 posiciones:", array)
    st.write(f"La suma de todos los valores es: {suma}")
    st.write(f"La media de todos los valores es: {media:.2f}")

if __name__ == "__main__":
    main()
