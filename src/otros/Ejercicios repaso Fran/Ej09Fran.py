# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

def MCD(a, b):

    while b != 0:
        temp = b
        b = a % b
        a = temp
    
    return a

def main():

    a = int(input("Introduce un el primer número: "))
    b = int(input("Introduce el segundo número: "))

    print(MCD(a, b))

if __name__ == "__main__":
    main()