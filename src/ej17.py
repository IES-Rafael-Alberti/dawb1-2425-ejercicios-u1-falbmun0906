# Ejercicio 1.2.17
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = str(input("Introduce tu nombre: "))
n = int(input("Introduce el número de veces que quieres que se repita: "))

print(f"{nombre}\n" * n)

"""
# Con bucle for

for i in range(1,n + 1):
    print(nombre)

"""