"""
Programa: Diagnóstico de Estado de Ánimo
Objetivo: Preguntar al usuario cómo se siente en distintas áreas
(estado de ánimo general, cansancio y preocupaciones) y, utilizando
condicionales, entregar una recomendación personalizada para cada
respuesta y un diagnóstico final.
"""


def diagnosticar_estado_animo(estado):
    """
    Evalúa el estado de ánimo general del usuario y devuelve
    una recomendación acorde a la respuesta entregada.
    """
    estado = estado.strip().lower()

    if estado == "feliz":
        return "¡Qué bueno! Sigue disfrutando tu día y comparte tu buena energía."
    elif estado == "triste":
        return "Lamento que te sientas así. Intenta hablar con alguien de confianza o sal a caminar."
    elif estado == "estresado":
        return "Respira profundo unos minutos y trata de organizar tus pendientes por prioridad."
    elif estado == "cansado":
        return "Tu cuerpo te está pidiendo descanso, intenta tomar una siesta corta o dormir temprano."
    else:
        return "Gracias por compartir cómo te sientes, recuerda que está bien no estar bien siempre."


def diagnosticar_cansancio(cansado):
    """
    Evalúa el nivel de cansancio del usuario (respuesta sí/no)
    y devuelve una recomendación acorde.
    """
    cansado = cansado.strip().lower()

    if cansado in ("si", "sí"):
        return "Trata de hacer una pausa, hidrátate y descansa la vista unos minutos."
    else:
        return "¡Excelente! Aprovecha tu energía para avanzar en tus tareas pendientes."


def diagnosticar_preocupacion(preocupado):
    """
    Evalúa si el usuario tiene preocupaciones y devuelve
    una recomendación acorde.
    """
    preocupado = preocupado.strip().lower()

    if preocupado in ("si", "sí"):
        return "Escribe tus preocupaciones en un papel, esto ayuda a ordenar tus ideas y bajar la ansiedad."
    else:
        return "Qué bien que estés tranquilo/a, sigue disfrutando ese estado de calma."


def generar_diagnostico_final(estado, cansado, preocupado):
    """
    Genera una conclusión general combinando las tres respuestas
    del usuario, usando condicionales para personalizar el mensaje.
    """
    estado = estado.strip().lower()
    cansado = cansado.strip().lower()
    preocupado = preocupado.strip().lower()

    if estado in ("triste", "estresado") and cansado in ("si", "sí") and preocupado in ("si", "sí"):
        return "Diagnóstico general: Necesitas una pausa real. Te recomendamos relajarte, desconectar un rato y descansar."
    elif estado == "feliz" and cansado == "no" and preocupado == "no":
        return "Diagnóstico general: ¡Todo marcha muy bien! Sigue así."
    elif cansado in ("si", "sí"):
        return "Diagnóstico general: Prioriza el descanso, tu cuerpo lo necesita."
    else:
        return "Diagnóstico general: Haz una pausa, sal a caminar un momento y vuelve con la mente más fresca."


def ejecutar_diagnostico():
    """
    Función principal: realiza las preguntas al usuario y
    muestra las recomendaciones y el diagnóstico final.
    """
    print("=" * 50)
    print("   PROGRAMA: DIAGNÓSTICO DE ESTADO DE ÁNIMO")
    print("=" * 50)

    # Pregunta 1: estado de ánimo general
    estado = input("¿Como te sientes hoy? (feliz / triste / estresado / cansado): ")
    print("->", diagnosticar_estado_animo(estado))
    print("-" * 50)

    # Pregunta 2: nivel de cansancio
    cansado = input("¿Te sientes cansado/a en este momento? (si/no): ")
    print("->", diagnosticar_cansancio(cansado))
    print("-" * 50)

    # Pregunta 3: preocupaciones
    preocupado = input("¿Tienes alguna preocupación en este momento? (si/no): ")
    print("->", diagnosticar_preocupacion(preocupado))
    print("-" * 50)

    # Diagnóstico final combinando las tres respuestas
    print(generar_diagnostico_final(estado, cansado, preocupado))
    print("=" * 50)


if __name__ == "__main__":
    ejecutar_diagnostico()
