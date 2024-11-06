import streamlit as st

def rellenar_array_streamlit(tamano):
    array = []
    st.write("Ingrese los números para llenar el array:")
    for i in range(tamano):
        num = st.number_input(f"Ingrese el número {i + 1}:", key=f"num_{i}", step=1)
        array.append(int(num))
    return array

def copiar_array(array):
    return array.copy()

def mostrar_array(array):
    st.write("Contenido del array:", array)

def ordenar_burbuja(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# Ejecución del programa en Streamlit
def main():
    st.title("Ejercicio 6: Métodos de Ordenación de Arrays")

    # Variables y opciones
    array = []
    array_copia = []

    # Seleccionar tamaño del array y rellenar el array
    tamano = st.number_input("Ingrese el tamaño del array:", min_value=1, step=1)
    if st.button("Rellenar array"):
        array = rellenar_array_streamlit(tamano)
        st.write("Array rellenado:", array)

    # Copiar el array
    if st.button("Copiar array"):
        array_copia = copiar_array(array)
        st.write("Array copiado:", array_copia)

    # Mostrar el array actual
    if st.button("Mostrar array"):
        mostrar_array(array)

    # Ordenar el array por burbuja
    if st.button("Ordenar array por burbuja"):
        array_ordenado = ordenar_burbuja(array)
        st.write("Array ordenado:", array_ordenado)

if __name__ == "__main__":
    main()
