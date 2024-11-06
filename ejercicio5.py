import streamlit as st

def crear_array_streamlit(tamano):
    array = []
    st.write("Ingrese los números para llenar el array:")
    for i in range(tamano):
        num = st.number_input(f"Ingrese el número {i + 1}:", key=f"num_{i}", step=1)
        array.append(int(num))
    return array

def encontrar_mayor(array):
    return max(array)

# Ejecución del programa en Streamlit
def main():
    st.title("Ejercicio 7: Encontrar el Mayor en un Array")

    # Seleccionar tamaño del array y rellenar el array
    tamano = st.number_input("Ingrese el tamaño del array:", min_value=1, step=1)

    # Rellenar el array y calcular el número mayor
    if tamano > 0:
        array = crear_array_streamlit(tamano)
        if st.button("Encontrar el número mayor"):
            mayor = encontrar_mayor(array)
            st.write(f"El número mayor en el array es: {mayor}")

if __name__ == "__main__":
    main()
