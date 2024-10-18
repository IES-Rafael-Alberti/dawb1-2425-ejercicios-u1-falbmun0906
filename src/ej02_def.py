# Ejercicio 1.2.2
# Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
# DEFINITIVO

def salario(horas, coste):
    total = horas * coste
    return total

def main():
    horas = int(input("Horas de trabajo: "))
    coste = int(input("Coste por hora: "))
    print(f"Importe total: {salario(horas, coste)}")

if __name__ == "__main__":
    main()