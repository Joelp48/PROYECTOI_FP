import streamlit as st

def crear_array_multiplos(x):
    # Crear un array con los múltiplos de X entre 0 y 100
    multiplos = [i for i in range(0, 101) if i % x == 0]

    # Retornar la cantidad de datos y la sumatoria de los datos
    cantidad_datos = len(multiplos)
    sumatoria_datos = sum(multiplos)

    return cantidad_datos, sumatoria_datos

# Ejecución del programa en Streamlit
def main():
    st.title("Ejercicio 4: Múltiplos de un Número")

    # Entrada del usuario
    x = st.number_input("Ingrese el valor de X (debe ser mayor que 0):", min_value=1, step=1)

    # Calcular y mostrar resultados al presionar el botón
    if st.button("Calcular"):
        cantidad, sumatoria = crear_array_multiplos(x)
        st.write(f"Cantidad de múltiplos de {x} entre 0 y 100: {cantidad}")
        st.write(f"Sumatoria de los múltiplos de {x} entre 0 y 100: {sumatoria}")

if __name__ == "__main__":
    main()

