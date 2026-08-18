# La Mazmorra del Dragón

# Variables iniciales
nombre = input("Introduce el nombre de tu héroe: ")
vida = 100      # entero
ataque = 15.5   # decimal
oro = 30        # entero

print(f"\n¡Bienvenido {nombre}! Comienzaras tu aventura con {vida} puntos de vida, {ataque} de ataque y {oro} monedas de oro.")

juego_continua = True

# Primer desafío: El guardia del puente
print("\nEl guardian del puente te bloquea el paso. ¿Qué harás?")
print("1. Atacar")
print("2. Sobornar con oro (30 monedas)")
print("3. Huir")

opcion = int(input("Elige una opción (1-3): "))


# - Si ataca, pierde algo de vida pero gana oro
# - Si soborna, resta oro y no pierde vida
# - Si huye, termina el juego


if opcion == 1:
    vida = vida - 30
    oro = oro + 40
    print("Atacaste al guardia.")
    print("Perdiste 30 puntos de vida, pero lograste conseguir 40 monedas de oro.")

elif opcion == 2:
    if vida > 50 and oro >= 30:
        oro = oro - 30
        vida = vida - 20
        print("Sobornaste al guardia y pudiste cruzar el puente, pero el guardia te hizo 20 puntos de daño.")

    else:
        print("No tienes la suficiente vida y oro para sobornar al guardia.")
        vida = vida - 25
        print("El guardia te atacó y perdiste 25 puntos de vida. Pero logras cruzar el puente.")

elif opcion == 3:
    print("Huiste de la mazmorra.")
    juego_continua = False

else:
    print("Opción no válida.")
    juego_continua = False

if vida <= 0:
    print("Has perdido todos tus puntos de vida.")
    juego_continua = False


# Segundo desafío: Sala de trampas
if juego_continua:

    print("\nLlegas a una sala oscura... !ten cuidado pueden haber trampas ocultas!")
    # Usar operadores de comparación y aritméticos para simular daño o esquiva
    # Ejemplo: si el oro es mayor a cierto valor, puede comprar una antorcha y evitar daño

    print("Hay una antorcha en un estante. Puedes comprarla por 10 monedas de oro para iluminar el camino y evitar trampas ¿Que haras?")
    print("1. Comprar la antorcha")
    print("2. Atravesar el pasillo sin la antorcha")

    opcion_trampa = int(input("Elige una opción (1-2): "))


    if opcion_trampa == 1:
        if oro >= 10:
            oro = oro - 10
            print("Has comprado la antorcha y lograste esquivar las trampas con exito.")
        else:
            vida = vida - 30
            print("No tienes suficiente oro. Una trampa te golpeó.")

    elif opcion_trampa == 2:
        vida = vida - 25
        print("Lograste atravesar el pasillo, pero una trampa te hizo 25 puntos de daño.")

    else:
        print("Opción no válida.")
        juego_continua = False

    if vida <= 0:
        print("Las trampas acabaron con tus puntos de vida.")
        juego_continua = False


#Tercer desafío: El dragón final
if juego_continua:

    print("\nFelicitaciones has llegado a la cámara final, pero aun te queda un último desafío ¡derrotar al dragón!")
    # Usar operadores aritméticos para calcular el daño infligido:
    # daño_total = ataque * multiplicador

    vida_dragon = 40
    dragon_derrotado = False

    print("1. Atacar al dragón")
    print("2. Huir")

    opcion_dragon = int(input("Elige una opción (1-2): "))

    # COMPLETAR: Lógica de combate con el dragón
    # --------------------------------

    if opcion_dragon == 1:

        multiplicador = 1.5
        daño_total = ataque * multiplicador

        vida_dragon = vida_dragon - daño_total

        print("Atacaste al dragón.")
        print("Le hiciste", daño_total, "puntos de daño.")
        print("Vida restante del dragón:", vida_dragon)

        # El dragón contraataca
        if vida_dragon > 0 and vida > 0:
            vida = vida - 50
            print("El dragón te atacó y perdiste 50 puntos de vida.")
            print("Tu vida restante es:", vida)

        # Segundo ataque
        if vida > 0 and vida_dragon > 0:
            print("\n¡Atacas nuevamente al dragón!")

            daño_total = ataque * 1.5
            vida_dragon = vida_dragon - daño_total

            print("Le hiciste", daño_total, "puntos de daño.")
            print("Vida restante del dragón:", vida_dragon)

        # Comprobar si el dragón fue derrotado
        if vida_dragon <= 0 and vida > 0:
            dragon_derrotado = True
            oro = oro + 100
            print("¡Derrotaste al dragón!, lograste conseguir 100 monedas de oro.")

        elif vida <= 0:
            print("El dragón te derrotó.")
            dragon_derrotado = False

        else:
            print("El dragón sigue con vida.")
            dragon_derrotado = False

    elif opcion_dragon == 2:
        print("Huiste del dragón.")
        dragon_derrotado = False
        juego_continua = False

    else:
        print("Opción no válida.")
        dragon_derrotado = False
        juego_continua = False

# Resultado final
# Mostrar si el héroe ganó (vida > 0 y dragón derrotado) o perdió

# COMPLETAR: Mensaje final
# --------------------------------

if dragon_derrotado and vida > 50:
    oro = oro * 2
    print("¡Bonus de supervivencia! Tu oro se duplicó.")

if vida > 0 and dragon_derrotado == True:
    print("\n¡GANASTE!")
    print("Lograste salir de la mazmorra con vida.")
    print("Oro final:", oro)
else:
    print("\n¡PERDISTE!")
    print("No lograste completar la mazmorra.")
