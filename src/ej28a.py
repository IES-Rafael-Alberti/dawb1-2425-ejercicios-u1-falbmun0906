
import math

def calcular_area(a: float, b: float, c: float) -> float:

    sp = (a + b + c) / 2
    area = math.sqrt(sp * (sp - a) * (sp - b) * (sp - c))

    return area

def comprobar_float(valor: str) -> bool:
    if valor.startswith("-"): # "-88.67"
        valor = valor[1:] # "88.67"

    pos_punto = valor.find(".") # 2

    if pos_punto >= 0:
        valor = valor[:pos_punto] + valor[pos_punto + 1:] #8867

    return valor.isdigit()

def introduce_numero(msj: str) -> float:
    valor = input(msj).strip().replace(",", ".")

    while not comprobar_float(valor):
        print("\n**ERROR** Número inválido!")
        valor = input(msj).strip().replace(",", ".")

    return float(valor)

def comprobar_triangulo(a, b, c) -> str:
    return (a + b > c) and (a + c > b) and (b + c > a)

def main():
    print("Dame los tres lados del triángulo...")
    lado_a = introduce_numero("Introduce el lado a: ")
    lado_b = introduce_numero("Introduce el lado b: ")
    lado_c = introduce_numero("Introduce el lado c: ")

    if comprobar_triangulo(lado_a, lado_b, lado_c): 
        area = calcular_area(lado_a, lado_b, lado_c)
        print("El área del triángulo con lados ({:.2f}, {:.2f}, {:.2f}) es {:.2f}.".format(lado_a, lado_b, lado_c, area))
    else:
        print("El triángulo con lados ({:.2f}, {:.2f}, {:.2f}) no es válido.".format(lado_a, lado_b, lado_c))

if __name__ == "__main__":
    main()