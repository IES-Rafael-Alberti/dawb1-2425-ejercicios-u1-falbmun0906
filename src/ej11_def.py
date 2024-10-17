# Ejercicio 1.2.11
# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: [operación dada]
# DEFINITIVO

# Con la operación dada

def suma(numero):

    total = int((numero * (numero + 1)) / 2)
    total = str(total)

    return total

def main():

    numero = int(input("Introduce un número entero: "))
    print(f"{suma(numero)} ({type(suma(numero))}")

if __name__ == "__main__":
    main()
