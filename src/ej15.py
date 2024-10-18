# Ejercicio 1.2.15
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

capital = float(input("Introduce la cantidad depositada: "))
TIPO = 4 / 100

# Interés = 4%

capital_anio1 = capital * (1 + TIPO)
capital_anio2 = capital_anio1 * (1 + TIPO)
capital_anio3 = capital_anio2 * (1 + TIPO)

print(f"El capital tras un año asciende a {capital_anio1:.2f}€, tras dos años a {capital_anio2:.2f}€ y tras tres años a {capital_anio3:.2f}€")

"""

# Con bucle for

capital_t = capital

for i in range(1, 4):
    capital_t = capital_t * (1 + 0.04)
    ahorro = capital_t - capital
    if i==1:
        print(f"El capital tras {i} año asciende a {capital_t:.2f}. En {i} año has ahorrado: {ahorro:.2f} euros.")
    else:
        print(f"El capital tras {i} años asciende a {capital_t:.2f}. En {i} años has ahorrado: {ahorro:.2f} euros.")
    
"""