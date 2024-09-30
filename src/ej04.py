# Ejercicio 1.2.4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida. 
# EXTRA: dos decimales.

temp_c = float(input("Introduce una temperatura en grados Celsius: ").replace(",", "."))
temp_f = ((9 / 5) * temp_c) + 32

# Para pasar de Celsius a Fahrenheit uso la fórmula °F = (9/5) * °C + 32

print(f"La temperatura en grados Fahrenheit es: {temp_f:.2f}ºF ({temp_c:.2f}ºC)")