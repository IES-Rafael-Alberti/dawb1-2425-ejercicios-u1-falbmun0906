# Ejercicio 1.2.11
# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: [operación dada]

n = int(input("Introduce un número entero: "))
suma = n

for i in range(1, n):
    suma += i

print("La suma de los",n,"primeros números es:", suma)

# Con la operación dada

n = int(input("Introduce otro número entero: "))

suma = int((n * (n + 1)) / 2)

print("La suma de los",n,"primeros números es:", suma)