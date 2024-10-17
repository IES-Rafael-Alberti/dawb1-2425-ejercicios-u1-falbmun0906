# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def saludo():

    nombre = input("Introduce tu nombre: ")
    return f"Hola, {nombre}."

def main():

    print(saludo())

if __name__ == "__main__":
    main()