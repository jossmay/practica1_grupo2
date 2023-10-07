# Importar la biblioteca math para usar la función de raíz cúbica
import math

# Función para calcular la potencia al cubo
def potencia_al_cubo(numero):
    return numero ** 3

# Función para calcular la raíz cúbica
def raiz_cubica(numero):
    return math.pow(numero, 1/3)

# Solicitar al usuario ingresar un número
try:
    numero = float(input("Por favor, ingresa un número: "))

    # Calcular y mostrar la potencia al cubo
    resultado_potencia = potencia_al_cubo(numero)
    print(f"La potencia al cubo de {numero} es: {resultado_potencia}")

    # Calcular y mostrar la raíz cúbica
    resultado_raiz = raiz_cubica(numero)
    print(f"La raíz cúbica de {numero} es: {resultado_raiz}")

except ValueError:
    print("Por favor, ingresa un número válido.")
