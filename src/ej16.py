# Ejercicio 1.2.16
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.

PRECIO_PAN = 3.49
precio_pan_nd = PRECIO_PAN * 0.40

numero_pan_nd = int(input("Introduce el número de barras de pan que no son del día: "))

print(f"El precio del pan es de {PRECIO_PAN:.2f}€.\nSe aplicará un descuento del 60% a las barras que no son del día.\nEl importe total a pagar es de", round(numero_pan_nd * precio_pan_nd, 2),"€.")