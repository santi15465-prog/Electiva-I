nombre1 = input("Ingrese el nombre del primer artículo: ")
# Solicita la cantidad de unidades del primer artículo
cantidad1 = int(input("Ingrese la cantidad: "))
# Solicita el precio de una unidad del primer artículo
precio1 = float(input("Ingrese el precio por unidad: "))
# Calcula el total de la venta del primer artículo
total1 = cantidad1 * precio1

nombre2 = input("Ingrese el nombre del segundo artículo: ")
# Solicita la cantidad de unidades del segundo artículo
cantidad2 = int(input("Ingrese la cantidad: "))
# Solicita el precio de una unidad del segundo artículo
precio2 = float(input("Ingrese el precio por unidad: "))
# Calcula el total de la venta del segundo artículo
total2 = cantidad2 * precio2

nombre3 = input("Ingrese el nombre del tercer artículo: ")
# Solicita la cantidad de unidades del tercer artículo
cantidad3 = int(input("Ingrese la cantidad: "))
# Solicita el precio de una unidad del tercer artículo
precio3 = float(input("Ingrese el precio por unidad: "))
# Calcula el total de la venta del tercer artículo
total3 = cantidad3 * precio3

print("\n--- Resumen de Ventas ---\n")

# Muestra el nombre y el total de venta del primer artículo
print("Artículo:", nombre1)
print("Total de la venta:" + str(total1) + "\n")
# Muestra el nombre y el total de venta del segundo artículo
print("Artículo:", nombre2)
print("Total de la venta:" + str(total2) + "\n")
# Muestra el nombre y el total de venta del tercer artículo
print("Artículo:", nombre3)
print("Total de la venta:" + str(total3) + "\n")
# Suma los totales de los tres artículos
total_ventas = total1 + total2 + total3

print("\n---Total acumulado----")
# Muestra el valor total de todas las ventas
print(str(total_ventas))