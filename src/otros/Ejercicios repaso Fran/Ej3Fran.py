# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(numero):
     
    factorial = 0

    for i in range(1, numero + 1):
        factorial += i

    return factorial

def main():

    numero = int(input("Introduce un numero entero: "))
    print(f"El factorial de {numero} es {factorial(numero)}.")

if __name__ == "__main__":
    main()