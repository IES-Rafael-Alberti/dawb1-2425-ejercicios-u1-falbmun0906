# Ejercicio 1.2.1
# Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.
# DEFINITIVO


def saludo(nombre):

    return f"Hola, {nombre}."

def main():

    nombre = input('Escribe tu nombre: ')
    print(saludo(nombre))

if __name__ == "__main__":
    main()