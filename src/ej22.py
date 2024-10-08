# Ejercicio 1.2.22
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

"""
# A lo bruto. Almaceno la frase y con el bucle for construyo una nueva frase al final de la anterior.
# Como ahora tengo dos frases (una seguida de la otra), elimino la original con slicing.

frase = str(input("Introduce una frase: "))
vocal = input("Introduce una vocal: ")

for letra in frase:
    if letra == vocal:
        frase += vocal.upper()
    else:
        frase += letra

print(frase[int((len(frase)) / 2):])

"""

# Con .replace

frase = str(input("Introduce una frase: "))
vocal = input("Introduce una vocal: ")

frase = frase.replace(vocal, vocal.upper())

print(frase)