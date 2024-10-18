# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.


def area_circulo(radio):

    PI = 3.14
    area = PI * (radio ** 2)

    return area

def volumen_cilindro(radio, altura):

    volumen = area_circulo(radio) * altura

    return volumen

def main():

    radio = float(input("Introduce el radio del círculo: "))
    altura = float(input("Introduce la altura del cilindro: "))

    print(f"El volumen del cilindro, para un radio de {radio} y una altura de {altura}, es: {volumen_cilindro(radio, altura)}.")

if __name__ == "__main__":
    main()