# Ejercicio 1.29
# Realiza un programa en Python que solicite un nombre y una edad.
# Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
# El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".

nombre = str(input("Introduce tu nombre: "))

if len(nombre) == 0:
    print("Desconocido")
else:
    edad = int(input("Introduce tu edad: "))
    while edad > 125 or edad <= 0:
        edad = input("Introduce una edad válida (entre 0 y 125 años): ")

    restante_vida = 125 - edad

# Control de la 's' en la palabra 'años'.

    if edad == 1:
        print(f"Te llamas {nombre} y tienes {edad} año, te quedan aún {restante_vida} años por cumplir.")
    else:
        if restante_vida == 1:
            print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {restante_vida} año por cumplir.")
        else:
            print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {restante_vida} años por cumplir.")
