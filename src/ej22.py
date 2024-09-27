# Ejercicio 1.2.22
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = str(input("Introduce una frase: "))
vocal = input("Introduce una vocal: ")

for letra in frase:
    if letra == vocal:
        frase += vocal.upper()
    else:
        frase += letra

print(frase[int((len(frase)) / 2):])