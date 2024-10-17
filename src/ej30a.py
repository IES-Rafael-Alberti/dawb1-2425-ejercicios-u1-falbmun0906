# Ejercicio 1.2.30

# Escribir un programa que determine si un número es primo

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

def es_primo():
    numero = dame_numero()
    cont = 2

    for i in range(1, numero + 1):
        if numero % i == 0:
            cont -= 1

    if cont >= 0:
        return True, numero
    else:
        return False, numero

def main():

    primo, numero = es_primo()

    if primo:
        print(f"El {numero} es primo.")
    else:
        print(f"El {numero} no es primo.")

if __name__ == "__main__":
    main()