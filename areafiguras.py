import sys
import math

def CalcularAreaDeCirculo(radio):
    return math.pi * radio ** 2

def CalcularAreaRectangulo(largo, ancho):
    return largo * ancho

def CalcularAreaDeTriangulo(base, altura):
    return (base * altura) / 2

def main():
    if len(sys.argv) < 3:
        print("Uso: python programa.py figura parametros...")
        sys.exit(1)

    figura = sys.argv[1].lower()
    parametros = sys.argv[2:]

    if figura == "circulo":
        areas = []
        for i, param in enumerate(parametros):
            if param.startswith("radio="):
                radio = float(param.split("=")[1])
                area = CalcularAreaDeCirculo(radio)
                areas.append(area)
                print(f"Área del círculo {i + 1} = {area:.2f}")

    elif figura == "rectangulo":
        areas = []
        for i, param in enumerate(parametros):
            if "largo=" in param and "ancho=" in param:
                largo = float(param.split("largo=")[1].split(",")[0])
                ancho = float(param.split("ancho=")[1])
                area = CalcularAreaRectangulo(largo, ancho)
                areas.append(area)
                print(f"Área del rectángulo {i + 1} = {area:.2f}")

    else:
        print("Figura no reconocida")

if __name__ == "_main_":
    main()

