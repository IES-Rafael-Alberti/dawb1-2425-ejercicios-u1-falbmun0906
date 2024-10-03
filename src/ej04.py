# Ejercicio 1.2.4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida. 
# EXTRA: dos decimales.

temp_c = float(input("Introduce una temperatura en grados Celsius: ").replace(",", "."))
temp_f = temp_c * 9/5 + 32

print(f"La temperatura en grados Fahrenheit es: {temp_f:.2f}ºF")