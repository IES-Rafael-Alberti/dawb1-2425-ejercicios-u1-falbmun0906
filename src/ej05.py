# Ejercicio 1.2.5
# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.

# El precio final será el importe sin IVA más este  multiplicado por el tipo de IVA

def precio_final(importe, tipo):
    total = importe + (importe * tipo)
    return total

def main():
    importe = float(input("Introduce el importe sin IVA: "))
    tipo = (int(input("Introduce el tipo de IVA a aplicar: ")) / 100)
    print(f"El precio final del artículo es: {precio_final(importe, tipo)}")

if __name__ == "__main__":
    main()