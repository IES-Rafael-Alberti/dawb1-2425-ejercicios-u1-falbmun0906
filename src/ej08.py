# Ejercicio 1.2.8
# Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

numero = float(input("Introduce el primer número: "))
suma = numero + float(input("Introduce el segundo número: "))
suma = suma + float(input("Introduce el tercer número: "))

print(f"El resultado de la suma de esos tres números es {suma}")

"""
# Con bucle for

for _ in range(2):
    numero = int(input("Introduce el segundo número: "))
    suma += numero

print("La suma de los tres números es: ", suma)

"""