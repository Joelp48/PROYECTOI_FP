import streamlit as st

def crear_array_streamlit():
    array = []
    st.write("Ingrese 10 números para llenar el array:")
    for i in range(10):
        num = st.number_input(f"Ingrese el número en la posición {i}:", key=f"num_{i}", step=1)
        array.append(int(num))
    return array

def mostrar_array_y_sumatoria(array):
    sumatoria = sum(array)
    st.write("Contenido del array con sus índices y valores:")
    for i, valor in enumerate(array):
        st.write(f"Índice {i}: Valor {valor}")
    st.write(f"\nLa sumatoria de los valores en el array es: {sumatoria}")

# Ejecución del programa en Streamlit
def main():
    st.title("Ejercicio 9: Array con Índices y Sumatoria")

    # Rellenar el array con 10 valores
    array = crear_array_streamlit()
    
    # Mostrar el array y la sumatoria cuando se presiona el botón
    if st.button("Mostrar índice, valor y sumatoria"):
        mostrar_array_y_sumatoria(array)

if __name__ == "__main__":
    main()
