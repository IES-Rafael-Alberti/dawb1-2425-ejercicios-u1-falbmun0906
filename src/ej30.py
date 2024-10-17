# Ejercicio 1.30
# Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.
# El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
# Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10

def serie(numero_inicial, numero_final, incremento):

    while numero_inicial <= 0 or incremento <= 0:
        print("El incremento y el total deben ser mayores que cero.")
        if numero_inicial == 0:
            numero_final = int(input("Introduce un número final de la serie válido: "))
        else:
            incremento = int(input("Introduce un valor del incremento válido: "))

    if numero_inicial > numero_final:
        serie = list(range(numero_inicial, numero_final - 1, -incremento))
    else:
        serie = list(range(numero_inicial, numero_final + 1, incremento))
    
    serie = "-".join(map(str, serie))
    return serie

def main():

    numero_inicial = int(input("Introduce el número inicial de la serie: "))
    numero_final = int(input("Introduce el número final de la serie: "))
    incremento = int(input("Introduce el valor del incremento: "))
    print(f"SERIE ==> {serie(numero_inicial, numero_final, incremento)}")

if __name__ == "__main__":
    main()