# Ejercicio 1.2.26
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

compra = input("Introduce los productos de la cesta de la compra, separados por ',': ").replace(", ",",") # Por si se introducen los productos con espacios (P.E: "pan, leche, agua..."")
compra = compra.split(",")
lista = "\n".join(compra)

print(lista.title())

"""
# Con bucle for

for i in range(0, len(compra)):
    print(f"{i + 1}. {compra[i].title()}")

"""