# Ejercicio 1.2.6
# Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

# El importe total es el 110% del importe sin IVA
# importe_iva = 10% del precio sin IVA entre el 110% del precio total

def importe_sin_iva(importe, importe_iva):
    importe_sin_iva = importe - importe_iva
    return importe_sin_iva

def main():
    importe = float(input("Introduce el importe tras IVA: ").replace(",","."))
    importe_iva = importe * (10/110)

    print(f"De ese importe {importe_iva:.2f} se corresponde al IVA, y {importe_sin_iva(importe, importe_iva):.2f} al precio sin IVA.")

if __name__ == "__main__":
    main()