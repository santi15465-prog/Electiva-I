#Fijar el salario semanal de tres empleados, considerando horas ordinarias y horas extras.
# Cantidad de horas ordinarias permitidas
HORAS_ORDINARIAS = 42.0

# Factor de multiplicación para horas extras
HORAS_EXTRAS = 1.50

empleado1 = input("Ingrese el nombre del empleado 1: ")
horas1 = float(input("Ingrese las horas trabajadas: "))
tarifa1 = float(input("Ingrese la tarifa por hora: "))

# Calcula las horas extras trabajadas por el empleado
extras1 = max(0.0, horas1 - HORAS_ORDINARIAS)

# Calcula las horas trabajadas de forma regular
regulares1 = horas1 - extras1

# Calcula el salario total incluyendo horas regulares y horas extras
salario1 = (regulares1 * tarifa1) + (extras1 * tarifa1 * HORAS_EXTRAS)

empleado2 = input("Ingrese el nombre del empleado 2: ")
horas2 = float(input("Ingrese las horas trabajadas: "))
tarifa2 = float(input("Ingrese la tarifa por hora: "))

extras2 = max(0.0, horas2 - HORAS_ORDINARIAS)
regulares2 = horas2 - extras2
salario2 = (regulares2 * tarifa2) + (extras2 * tarifa2 * HORAS_EXTRAS)

empleado3 = input("Ingrese el nombre del empleado 3: ")
horas3 = float(input("Ingrese las horas trabajadas: "))
tarifa3 = float(input("Ingrese la tarifa por hora: "))

extras3 = max(0.0, horas3 - HORAS_ORDINARIAS)
regulares3 = horas3 - extras3
salario3 = (regulares3 * tarifa3) + (extras3 * tarifa3 * HORAS_EXTRAS)

total_nomina = salario1 + salario2 + salario3

print("\n--- Resumen de Salarios ---\n")
# Muestra el salario total de cada empleado
print("Salario total de " + empleado1 + ": $" + str(salario1) + "\n")
print("Salario total de " + empleado2 + ": $" + str(salario2) + "\n")
print("Salario total de " + empleado3 + ": $" + str(salario3) + "\n")

# Muestra el total de la nómina
print("Total a pagar a todos los empleados: $" + str(total_nomina))
