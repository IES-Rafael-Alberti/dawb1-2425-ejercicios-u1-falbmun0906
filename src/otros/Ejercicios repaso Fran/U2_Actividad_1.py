# Escribe un programa que lea repetidamente números hasta que el usuario introduzca "fin". Una vez se haya introducido "fin", muestra por pantalla el total, la cantidad de números y la media de esos números. Si el usuario inntroduce cualquier otra cosa que no sea un número, (más adelante veremos como detectar los fallos usando try y except).

def dame_numero() -> str:

    numero = input("Introduce un número: ")

    if numero.lower() == "fin":
        return numero
    else:
        return comprobar_numero(numero)

def comprobar_numero(numero):

    try:
        numero = int(numero)
    except ValueError:
        print("**ERROR DE FORMATO**")
        numero = dame_numero()

    return str(numero)

def main():
    numero = ""
    numeros = []

    while numero.lower() != "fin":
        numero = dame_numero()
        if numero.lower() == "fin":
            continue
        else:
            numeros.append(numero)
    
    numeros = list(map(int, numeros))

    total = 0

    for n in numeros:
        total += n

    if len(numeros) > 0:
        media = total / len(numeros)

    print(f"{total}, {len(numeros)}, {media}")

if __name__ == "__main__":
    main()