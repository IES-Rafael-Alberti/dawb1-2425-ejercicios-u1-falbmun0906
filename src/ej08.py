# Ejercicio 1.2.8
# Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

numero = int(input("Introduce el primer número: "))
suma = numero

for _ in range(2):
    numero = int(input("Introduce el segundo número: "))
    suma += numero

print("La suma de los tres números es: ", suma)