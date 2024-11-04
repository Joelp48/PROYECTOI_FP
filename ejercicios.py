import streamlit as st

def ingresar_datos():
    marca = st.text_input("Ingrese la marca del automóvil:")
    modelo = st.text_input("Ingrese el modelo del automóvil:")
    kilometraje = st.text_input("Ingrese el kilometraje del automóvil:")

    # Validación de campos vacíos
    if not marca:
        st.error("Error: La marca no puede estar vacía.")
        return None
    if not modelo:
        st.error("Error: El modelo no puede estar vacío.")
        return None
    if not kilometraje:
        st.error("Error: El kilometraje no puede estar vacío.")
        return None

    # Validación de kilometraje como un número no negativo
    try:
        kilometraje = float(kilometraje)
        if kilometraje < 0:
            st.error("Error: El kilometraje no puede ser menor que 0.")
            return None
    except ValueError:
        st.error("Error: El kilometraje debe ser un número.")
        return None

    return {
        "Marca": marca,
        "Modelo": modelo,
        "Kilometraje": kilometraje
    }

# Ejecución del programa
def main():
    st.title("Ingreso de Datos de Automóvil")
    datos_auto = ingresar_datos()
    if datos_auto:
        st.success("Datos del automóvil ingresados correctamente:")
        st.write(datos_auto)

if __name__ == "__main__":
    main()

