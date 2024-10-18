# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def media(numeros):
    
    lista_float = list(map(float, numeros))
    resultado = 0

    for n in lista_float:
        resultado = resultado + n

    media = resultado / len(numeros)

    return media

def main():

    numeros = input("Introduce una serie de números separados por comas: ").replace(" ","")
    numeros = numeros.split(",")

    print(f"La media de los números introducidos es: {media(numeros)}")

if __name__ == "__main__":
    main()