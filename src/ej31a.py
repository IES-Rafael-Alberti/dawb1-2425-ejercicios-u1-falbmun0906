# Ejercicio 1.2.31

# Mostrar todos los divisores de un número

def dame_numero():
    numero = comprobar_numero(input("Introduce un número entero: "))

    return numero

def comprobar_numero(numero):
    salir = False
    while salir != True:
        try:
            numero = int(numero)
            salir = True
        except:
            print("**ERROR**")
            numero = dame_numero()

    return numero

def calcular_divisores():

    numero = dame_numero()
    divisores = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(numero / i)

    return numero, divisores

def main():

    numero, divisores = calcular_divisores()

    print(f"Los divisores de {numero} son: {list(map(int, divisores))}")

if __name__ == "__main__":
    main()