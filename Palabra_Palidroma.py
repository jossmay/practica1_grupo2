def es_palindromo(palabra):
    # Elimina espacios en blanco y convierte la palabra a minúsculas
    palabra = palabra.replace(" ", "").lower()

    # Comprueba si la palabra es igual a su inversa
    if palabra == palabra[::-1]:
        return True
    else:
        return False


def main():
    palabra = input("Ingresa una palabra: ")

    if es_palindromo(palabra):
        print(f"'{palabra}' es un palíndromo.")
    else:
        print(f"'{palabra}' no es un palíndromo.")


if __name__ == "__main__":
    main()

def es_palabra_aguda(palabra):
    # Convierte la palabra a minúsculas para facilitar la comparación
    palabra = palabra.lower()
    
    # Define una lista de vocales acentuadas
    vocales_acentuadas = ['á', 'é', 'í', 'ó', 'ú']
    
    # Verifica si la última letra de la palabra es una vocal acentuada
    if palabra[-1] in vocales_acentuadas:
        return True
    else:
        return False

# Ejemplos de uso:
palabra1 = "canción"
palabra2 = "computadora"

if es_palabra_aguda(palabra1):
    print(f'La palabra "{palabra1}" es aguda.')
else:
    print(f'La palabra "{palabra1}" no es aguda.')

if es_palabra_aguda(palabra2):
    print(f'La palabra "{palabra2}" es aguda.')
else:
    print(f'La palabra "{palabra2}" no es aguda.')
