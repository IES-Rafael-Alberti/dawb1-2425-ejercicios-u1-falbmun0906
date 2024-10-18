# Ejercicio 1.2.5
# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
# DEFINITIVO

# El precio final será el importe sin IVA más este  multiplicado por el tipo de IVA

def precio_final(importe, tipo):
    
    importe_iva = importe + (importe * tipo)

    print(f"El importe tras IVA es: {importe_iva:.2f}")

def main():

    importe = float(input("Introduce el importe sin IVA: "))
    tipo = (int(input("Introduce el tipo de IVA a aplicar: ")) / 100)

    precio_final(importe, tipo)

if __name__ == "__main__":
    main()