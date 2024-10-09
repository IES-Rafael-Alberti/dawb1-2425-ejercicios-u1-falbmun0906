# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def cuadrados(numeros):

    cuadrados = list(map(float, numeros))
    cuadrados = list(map(lambda x: x ** 2, cuadrados))

    return cuadrados


def main():

    numeros = list(input("Introduce una serie de números separados por comas: ").replace(" ", "").split(","))

    print(f"La lista de cuadrados es: {cuadrados(numeros)}")

if __name__ == "__main__":
    main()