import math

def calcular_potencia_cubo(numero):
    return numero ** 3

def calcular_raiz_cubica(numero):
    return math.pow(numero, 1/3)

while True:
    print("Selecciona una opción:")
    print("1. Calcular potencia al cubo")
    print("2. Calcular raíz cúbica")
    print("3. Salir")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        numero = float(input("Ingrese un número para calcular su potencia al cubo: "))
        resultado = calcular_potencia_cubo(numero)
        print(f"El resultado es: {resultado}")
    elif opcion == "2":
        numero = float(input("Ingrese un número para calcular su raíz cúbica: "))
        resultado = calcular_raiz_cubica(numero)
        print(f"El resultado es: {resultado}")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
