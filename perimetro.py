def perimetro_triangulo(cateto1: float, cateto2: float) -> float:
    hipotenusa = calcular_hip(cateto1, cateto2)
    return cateto1 + cateto2 + hipotenusa

def calcular_hip(cateto1: float, cateto2: float) -> float:
    suma_cuadrados = (cateto1 * 2) + (cateto2 * 2)
    hipotenusa = pow(suma_cuadrados, 0.5)
    return hipotenusa

cadena_cat_1 = input("Indique la longitud del primer cateto: ")
cadena_cat_2 = input("Indique la longitud del segundo cateto: ")
cat_1 = float(cadena_cat_1)
cat_2 = float(cadena_cat_2)
perimetro = perimetro_triangulo(cat_1, cat_2)
print(f"El perímetro de un triángulo rectángulo que tenga catetos de longitud {cat_1} y {cat_2} es {perimetro}")
