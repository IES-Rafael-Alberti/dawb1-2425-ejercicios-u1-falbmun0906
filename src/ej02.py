## Ejercicio 1.2.2
## Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.

horas = int(input("Horas de trabajo: "))
coste = int(input("Coste por hora: "))
total = str(horas * coste)

print("Importe total: " + total)