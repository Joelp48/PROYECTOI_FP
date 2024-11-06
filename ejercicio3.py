import streamlit as st

def crear_array_streamlit(tamano):
    array = []
    st.write("Ingrese los números para llenar el array:")
    for i in range(tamano):
        num = st.number_input(f"Ingrese el número {i + 1}:", key=f"num_{i}", step=1)
        array.append(int(num))
    return array

def buscar_numero(array, numero_a_buscar):
    ocurrencias = array.count(numero_a_buscar)
    return ocurrencias

# Ejecución del programa en Streamlit
def main():
    st.title("Ejercicio 5: Búsqueda de un Número en un Array")

    # Ingresar el tamaño del array
    tamano = st.number_input("Ingrese el tamaño del array:", min_value=1, step=1)

    # Crear el array si el tamaño es válido
    if tamano > 0:
        array = crear_array_streamlit(tamano)
        
        # Ingresar el número a buscar
        numero_a_buscar = st.number_input("Ingrese el número a buscar:", step=1)
        
        # Botón para realizar la búsqueda
        if st.button("Buscar"):
            ocurrencias = buscar_numero(array, numero_a_buscar)
            st.write(f"El número {numero_a_buscar} se encontró {ocurrencias} veces en el array.")

if __name__ == "__main__":
    main()
