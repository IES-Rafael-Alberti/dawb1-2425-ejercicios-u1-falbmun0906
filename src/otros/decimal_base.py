
def dame_numero():

    numero = input("Introduce un número en base decimal: ").replace(",", ".")
    
    while True:
        try:
            numero = float(numero)
            break
        except ValueError:
            numero = input("Error: Introduce un número válido: ")

    numero_str = str(numero).split(".")
    parte_entera = numero_str[0]
    parte_decimal = numero_str[1]

    return parte_entera, parte_decimal

def convertir_base(parte_entera, parte_decimal):

    base = int(input("Introduce una base: "))
    decimales = int(input("Introduce el número de decimales que desea: "))
    parte_entera = int(parte_entera)
    parte_decimal = float(parte_decimal) / 100

    entero_binario = str("")
    decimal_binario = str("")

    cociente = parte_entera

    while cociente >= base:
        entero_binario += str(cociente % base)
        cociente = cociente // base
        if cociente < base:
            entero_binario += str(cociente)

    for i in range(0, decimales):
        parte_decimal = parte_decimal * base
        decimal_binario += str(int(parte_decimal))
        parte_decimal = parte_decimal - int(parte_decimal)

    return ".".join([entero_binario[::-1], decimal_binario])

def main():

    parte_entera, parte_decimal = dame_numero()
    resultado_binario = convertir_base(parte_entera, parte_decimal)

    print(f"{resultado_binario}")

if __name__ == "__main__":
    main()