# Ejercicio 1.2.6
# Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

importe = float(input("Introduce el importe tras IVA: "))
importe_iva = importe * (10/110)

# El importe total es el 110% del importe sin IVA
# importe_iva = 10% del precio sin IVA entre el 110% del precio total

print("De ese importe, ", round(importe_iva, 2), "se corresponde al IVA, y ", round(importe - importe_iva, 2), " al precio sin IVA.")