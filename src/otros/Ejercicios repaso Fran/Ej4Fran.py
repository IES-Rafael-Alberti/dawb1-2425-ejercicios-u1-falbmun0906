# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def factura(precio, tipo):

    precio = float(precio)
    tipo = float(tipo) / 100

    factura = precio + (precio * tipo)

    return factura

def main():

    precio = input("Introduce el precio sin IVA: ")
    tipo = input("Introduce el tipo de IVA: ")

    if tipo == "":
        tipo = 21

    print(f"El total de la factura es: {factura(precio, tipo):.2f}€")

if __name__ == "__main__":
    main()