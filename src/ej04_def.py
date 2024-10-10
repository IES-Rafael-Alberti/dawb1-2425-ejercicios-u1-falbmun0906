# Ejercicio 1.2.4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida. 
# EXTRA: dos decimales.
# DEFINITIVO

def conversion_a_celsius():
    temp_f = float(input("Introduce una temperatura en grados Fahrenheit: ").replace(",", "."))
    temp_c = (temp_f - 32) * (5 / 9)
    return f"La temperatura en grados Celsius es: {temp_c:.2f}ºC ({temp_f:.2f}ºF)"

def main():
    print(conversion_a_celsius())

if __name__ == "__main__":
    main()