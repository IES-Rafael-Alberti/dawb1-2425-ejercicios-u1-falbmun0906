import random

def limites():
    valor_max = input("Introduce el límite superior del rango: ")
    valor_min = input("Introduce el límite inferior del rango: ")
    if valor_max < valor_min:
        valor_min, valor_max = valor_max, valor_min

    rango = [valor_min, valor_max]

    return comprobar_int(rango)

def comprobar_int(rango):
    try:
        rango = list(map(int, rango))
    except ValueError:
        print("Error de formato.")
        rango = limites()
    
    return rango

def aleatorio():
    numero_aleatorio = random.randint(limites())

    return numero_aleatorio

def main():

    print(aleatorio())

if __name__ == "__main__":
    main()