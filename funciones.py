def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_term = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_term)
        return fib_sequence

#Se agrega funcion de numeros primos
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Ejemplo de uso:
numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")

# Potencia al cubo y raiz cubica
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
        print("Saliendo....")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

#Se agrega funcionalidad para calcular area de un triangulo

# Pedir al usuario que ingrese la base y la altura del triángulo
base = float(input("Ingrese la longitud de la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

# Calcular el área del triángulo
area = (base * altura) / 2

# Mostrar el resultado
print(f"El área del triángulo con base {base} y altura {altura} es: {area}")
