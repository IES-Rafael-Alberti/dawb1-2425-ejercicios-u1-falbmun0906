# Ejercicio 1.2.19
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre.

nombre = input("Introduce tu de usuario: ")
nombre_apellidos = nombre.replace(" ","")

# En el caso en que se introduzca un nombre con apellidos, elimino los espacios entre los elementos para que solo cuente las letras.

print(f"{nombre.upper()} tiene {len(nombre_apellidos)} letras")