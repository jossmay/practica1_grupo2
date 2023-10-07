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
