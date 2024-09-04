# Bucle para asegurar que n sea un número entero positivo
while True:
    entrada = input("Ingrese un número entero positivo (o 'q' para salir): ")
    if entrada.lower() == 'q':
        print("Saliendo del programa.")
        exit()
    try:
        n = int(entrada)
        if n > 0:
            break  # Sale del bucle si n es un número válido
        else:
            print("El número debe ser un entero positivo. Inténtelo de nuevo.")
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")

# Bucle para asegurar que b sea un número entero positivo entre 2 y 9
while True:
    entrada = input("Ingrese la base (debe ser un número entero positivo menor que 10): (o 'q' para salir): ")
    if entrada.lower() == 'q':
        print("Saliendo del programa.")
        exit()
    try:
        b = int(entrada)
        if 1 < b < 10:
            break  # Sale del bucle si b es una base válida
        else:
            print("La base debe ser un número mayor que 1 y menor que 10. Inténtelo de nuevo.")
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")

# Convertir el número n a la base b
resultado = ""  # Cadena para almacenar el número en la nueva base
while n > 0:
    residuo = n % b  # Calcula el residuo de n dividido por b
    resultado = str(residuo) + resultado  # Añade el residuo al resultado
    n = n // b  # Actualiza n dividiéndolo por b
    print(f"Residuo: {residuo}, Nuevo valor de n: {n}")

# Mostrar el resultado final
print(f"El número en base {b} es: {resultado}")
