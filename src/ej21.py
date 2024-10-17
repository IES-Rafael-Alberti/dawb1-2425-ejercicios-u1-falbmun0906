# Ejercicio 1.2.21
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

frase = str(input("Introduce una frase: "))

print(frase[::-1])

""" 
## Con reversed() creo un iterable y con ''.join() uno los elementos en una cadena.

frase_invertida = ''.join(reversed(frase))

print(frase_invertida)

"""