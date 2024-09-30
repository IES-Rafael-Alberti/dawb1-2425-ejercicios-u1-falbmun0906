# Ejercicio 1.2.12
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("Introduce tu peso (kg): ").replace(",","."))
estatura = float(input("Introduce tu estatura (m): ").replace(",","."))

# IMC = peso (kg)/ [estatura (m)]^2

imc = (peso) / ((estatura) ** 2)

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")