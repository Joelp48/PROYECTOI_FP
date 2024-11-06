def crear_array_multiplos(x):
    # Crear un array con los múltiplos de X entre 0 y 100
    multiplos = [i for i in range(0, 101) if i % x == 0]

    # Retornar la cantidad de datos y la sumatoria de los datos
    cantidad_datos = len(multiplos)
    sumatoria_datos = sum(multiplos)

    return cantidad_datos, sumatoria_datos

# Ejemplo de uso
def main():
    try:
        x = int(input("Ingrese el valor de X: "))
        if x <= 0:
            print("El valor de X debe ser mayor que 0.")
            return
        cantidad, sumatoria = crear_array_multiplos(x)
        print(f"Cantidad de múltiplos de {x} entre 0 y 100: {cantidad}")
        print(f"Sumatoria de los múltiplos de {x} entre 0 y 100: {sumatoria}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
