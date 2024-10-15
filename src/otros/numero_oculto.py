import random

def rango():
    limites = input("Introduce el rango (X-Y): ")
    
    # VALIDACIÓN
    salir = False

    while not salir:
        if limites.count("-") == 1:
            try:
                limites = list(map(int, limites.split("-")))
                if limites[0] > limites[1]:
                    limites[0], limites[1] = limites[1], limites[0]
                print(f"Rango: {limites}")
                
                salir = True

            except ValueError:
                limites = input("**ERROR** Formato incorrecto. Por favor, inténtalo de nuevo (X-Y): ")
        else:
            limites = input("**ERROR** Formato incorrecto. Por favor, inténtalo de nuevo (X-Y): ")
            
    return limites

def aleatorio():
    limites = rango()
    ran_num = random.randint(limites[0], limites[1])

    return ran_num, limites

def dame_numero(limites):
    salir = False

    while not salir:
        try:
            numero = int(input(f"Introduce un número entre {limites[0]} y {limites[1]}: "))
            if numero > limites[1] or numero < limites[0]:
                print("El número introducido está fuera de los límites.")
                continue
            else:
                salir = True
        except:
            print("**ERROR** Debes introducir un número entero.")
    
    return numero

def calcular_distancia(longitud_rango, ran_numero, numero):
    distancia_max = longitud_rango
    distancia_abs = abs(numero - ran_numero)
    distancia_rel = distancia_abs * 100 / distancia_max

    return distancia_rel

def juego():
    
    ran_numero, limites = aleatorio()
    longitud_rango = limites[1] - limites[0]
    intentos = 5
    numero = dame_numero(limites)
    
    while ran_numero != numero and intentos > 1:
        distancia_rel = calcular_distancia(longitud_rango, ran_numero, numero)

        if distancia_rel <= 5:
            print(f"¡¡ARDIENDO!! Te quedan {intentos} intentos.")
        elif 5 < distancia_rel <= 15:
            print(f"Caliente, caliente... Te quedan {intentos} intentos.")
        elif 15 < distancia_rel <= 30:
            print(f"Fresco... Te quedan {intentos} intentos.")
        elif 30 < distancia_rel <= 60:
            print(f"Frío, frío... Te quedan {intentos} intentos.")
        else:
            print(f"Congelado. Te quedan {intentos} intentos.")

        intentos -= 1
        numero = dame_numero(limites)
        
    if ran_numero == numero:
        return f"¡¡CORRECTO!! El número oculto es el {ran_numero}"
    else:
        return f"Has gastado los 5 intentos :( El número oculto era el {ran_numero}."

def main():

    print(juego())

if __name__ == "__main__":
    main()