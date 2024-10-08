

def dame_numero():

    numero1 = input("Introduce el primer número: ")
    numero2 = input ("Introduce el segundo número: ")

    while comprobar_numero(numero1, numero2) != True:
        print("Debes introducir números enteros.")
        numero1 = input("Introduce el primer número: ")
        numero2 = input ("Introduce el segundo número: ")
    
    return int(numero1), int(numero2)

def comprobar_numero(numero1, numero2):

    numero1 = numero1.strip()
    numero2 = numero2.strip()

    return ((numero1).isdigit() or (numero1).startswith("-") and (numero1)[1:].isdigit()) and ((numero2).isdigit() or (numero2).startswith("-") and (numero2)[1:].isdigit())

def comparar_numero(numero1, numero2):

    if numero1 > numero2:
        return numero1
    elif numero1 < numero2:
        return numero2
    else:
        return 0

def main():

    numero1, numero2 = dame_numero()

    print(f"El número mayor es: {comparar_numero(numero1, numero2)}")

if __name__ == "__main__":
    main()