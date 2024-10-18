
def convertir_a_binario(valor, base):

    cociente = valor
    resultado = ""

    while cociente >= 2:

        resto = cociente % base
        resultado += str(resto)
        cociente = cociente // base

    resultado += str(cociente)
    resultado = resultado[::-1]
    return resultado
        

def main():
    valor = int(input("Introduzca un número: "))
    base = int(input("Introduzca la base: "))

    print(f"{convertir_a_binario(valor, base)}")

if __name__ == "__main__":
    main()