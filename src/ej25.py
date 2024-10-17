# Ejercicio 1.2.25
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

"""
# Me aseguro de que se está introduciendo una fecha válida.

fecha = [0, 0, 0]
dia = fecha[0]
mes = fecha[1]
año = fecha[2]

while (dia < 1 or dia > 31) or (mes < 1 or mes > 12):
    
    fecha = input("Introduce tu fecha de nacimiento: ").split("/")

    if len(fecha) != 3:
        print("Por favor, introduce un formato de fecha válido (DD/MM/AA).")
        continue
    else:
        try:
            dia = int(fecha[0])
            mes = int(fecha[1])
            año = int(fecha[2])
            if (dia < 1 or dia > 31) or (mes < 1 or mes > 12):
                print("Fecha no válida. El día debe estar entre 1 y 31 y el mes entre 1 y 12.")
                continue
        
            break

        except ValueError:
            print("Fecha no válida. Debes usar números.")

print(f"{dia:02}/{mes:02}/{año:04}")

"""

fecha = input("Introduce tu fecha de nacimiento: ").split("/")
dia = int(fecha[0])
mes = int(fecha[1])
año = int(fecha[2])

print(f"{dia:02}/{mes:02}/{año:04}")