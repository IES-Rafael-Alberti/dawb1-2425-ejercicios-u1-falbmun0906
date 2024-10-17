# Ejercicio 1.2.32

# Calcular la serie de Fibonacci hasta un número dado

def dame_numero():
    numero = comprobar_numero(input("Introduce un número entero: "))

    return numero

def comprobar_numero(numero):
    salir = False
    while salir != True:
        try:
            numero = int(numero)
            salir = True
        except:
            print("**ERROR**")
            numero = dame_numero()

    return numero

def fib():

    numero = dame_numero() 
    serie = [0, 1]

    # Serie con numero = 6 -> 0 1 1 2 3 5

    while len(serie) < numero:
        print(serie[-1])
        serie.append(serie[-1] + serie[-2])
    return (serie)

def main():

    print(fib())

if __name__ == "__main__":
    main()