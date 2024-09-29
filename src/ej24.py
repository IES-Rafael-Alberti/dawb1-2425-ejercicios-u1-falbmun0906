# Ejercicio 1.2.24
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

while True:
    precio = str(input("Introduce el precio del producto: ").replace(",","."))
    try:
        precio = float(precio)
        break
    except ValueError:
        print("Precio no válido.")

precio_euros = int(precio)
precio_centimos = round((precio - precio_euros) * 100)

print(f"El producto cuesta {precio_euros} euros y {precio_centimos} céntimos")