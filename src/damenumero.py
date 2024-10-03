
def comprobar_entero(cadena: str):
    
    cadena = cadena.strip()
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit())

def dame_entero():

    cadena = input("Introduce un número entero: ")

    while not comprobar_entero(cadena):
        cadena = input("Eso no es un entero.\nIntrodúcelo bien: ")

    return int(cadena)

def main():
    num = dame_entero()
    print(f"Has introducido el número {num}")

if __name__ == "__main__":
    main()