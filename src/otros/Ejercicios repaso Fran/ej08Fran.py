# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

# def desviacion(numeros):

#     for i in numeros():



# def varianza():

def calculo_media(numeros):
    
    total = 0

    for i in numeros:
        total += i

    media = total / len(numeros)

    return media

def calculo_varianza(numeros):

    sumatorio = 0
    media = calculo_media(numeros)

    for i in numeros:
        sumatorio += ((i - media) ** 2)

    varianza = sumatorio / len(numeros)

    return varianza

def calculo_desviacion(numeros):

    

def diccionario(numeros):

    media = calculo_media(numeros)
    varianza = calculo_varianza(numeros)
    desviacion = calculo_deviacion(numeros)

def main():

    numeros = input("Introduce un serie de números separados por comas: ").replace(" ", "")
    numeros = list(map(int, numeros.split(",")))

    print(diccionario(numeros))

if __name__ == "__main__":
    main()