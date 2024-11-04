def ingresar_datos():
    marca = input("Ingrese la marca del automóvil: ").strip()
    modelo = input("Ingrese el modelo del automóvil: ").strip()
    kilometraje = input("Ingrese el kilometraje del automóvil: ").strip()

    # Validación de campos vacíos
    if not marca:
        print("Error: La marca no puede estar vacía.")
        return None
    if not modelo:
        print("Error: El modelo no puede estar vacío.")
        return None
    if not kilometraje:
        print("Error: El kilometraje no puede estar vacío.")
        return None

    # Validación de kilometraje como un número no negativo
    try:
        kilometraje = float(kilometraje)
        if kilometraje < 0:
            print("Error: El kilometraje no puede ser menor que 0.")
            return None
    except ValueError:
        print("Error: El kilometraje debe ser un número.")
        return None

    return {
        "Marca": marca,
        "Modelo": modelo,
        "Kilometraje": kilometraje
    }

# Ejecución del programa
def main():
    datos_auto = ingresar_datos()
    if datos_auto:
        print("Datos del automóvil ingresados correctamente:")
        print(datos_auto)

if __name__ == "__main__":
    main()
