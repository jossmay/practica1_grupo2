# Función para realizar la multiplicación
def multiplicar(a, b):
    return a * b

# Función para realizar la división
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."

while True:
    # Mostrar el menú
    print("Selecciona una operación:")
    print("1. Multiplicación")
    print("2. División")
    print("3. Salir")

    # Solicitar la elección del usuario
    opcion = input("Ingresa el número de la operación que deseas realizar: ")

    # Validar la entrada del usuario
    if opcion == '1':
        # Multiplicación
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = multiplicar(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == '2':
        # División
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
	if num2 == 0:
        	print("¡Cuidado! Estás dividiendo entre cero.")
    	else:
       		resultado = dividir(num1, num2)
		print("El resultado de la división es:", resultado)
    elif opcion == '3':
        # Salir del programa
        print("Saliendo.....")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
