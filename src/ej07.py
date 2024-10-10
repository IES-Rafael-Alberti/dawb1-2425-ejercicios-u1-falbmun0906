# Ejercicio 1.2.7
# Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

def suma(num1, num2, num3):

    total = num1 + num2 + num3
    return total

def main():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))

    print(f"La suma de los números introducidos es: {suma(num1, num2, num3)}")