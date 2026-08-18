def calcular_promedio(calificaciones):
    total = sum(calificaciones)
    promedio = total / len(calificaciones)
    return promedio

calificaciones = []
num_estudiantes = int(input("Ingrese el número de estudiantes: "))

for i in range(num_estudiantes):
    calificacion = float(input(f"Ingrese la calificación del estudiante {i+1}: "))
    calificaciones.append(calificacion)

promedio = calcular_promedio(calificaciones)
print("El promedio de las calificaciones es:", promedio)
