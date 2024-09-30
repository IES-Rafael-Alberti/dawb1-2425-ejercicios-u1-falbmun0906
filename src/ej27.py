# Ejercicio 1.2.27
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: ").replace(",","."))
cantidad = float(input("Introduce la cantidad a comprar: "))

print(f"Producto: {producto}. Precio: {precio:09.2f}. Total: {precio * cantidad:011.2f}")

"""
# Con validación de entrada.

producto = input("Introduce el nombre del producto: ")
precio = input("Introduce el precio del producto: ").replace(",",".") 

while True:
    try:
        precio = float(precio)
        break
    except:
        precio = input("Introduce un precio válido: ").replace(",",".")

cantidad = input("Introduce la cantidad a comprar: ")

while True:
    try:
        cantidad = float(cantidad)
        break
    except:
        cantidad = input("Introduce una cantidad válida: ").replace(",",".")

print(f"Producto: {producto}. Precio: {precio:09.2f}. Total: {precio * cantidad:011.2f}")

"""