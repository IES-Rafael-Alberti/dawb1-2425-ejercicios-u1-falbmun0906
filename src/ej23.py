# Ejercicio 1.2.23
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

email = str(input("Introduce tu correo electrónico: "))

email_ceu = email.replace((email.split("@")[1]), "ceu.es")

print("Tu correo institucional es:", email_ceu)