def solicitar_respuesta(intento):
    while True:
        respuesta = input(f"El número es {intento}? (responde 'mayor', 'menor' o 'igual'): ").strip().lower()
        if respuesta in ['mayor', 'menor', 'igual']:
            return respuesta
        print("Respuesta no válida. Por favor, responde 'mayor', 'menor' o 'igual'.")

# Establecemos los límites iniciales.
limite_inferior = 1
limite_superior = 100

# Iniciamos el juego.
print("Piensa en un número entre 1 y 100 y yo intentaré adivinarlo.")

# Como máximo, necesitaremos log2(100) intentos para adivinar el número.
for _ in range(7):  # log2(100) es aproximadamente 7
    # Calculamos el punto medio.
    intento = (limite_inferior + limite_superior) // 2
    
    # Obtenemos la respuesta del usuario.
    respuesta = solicitar_respuesta(intento)
    
    # Procesamos la respuesta del usuario.
    if respuesta == 'igual':
        print(f"¡He adivinado tu número! Es {intento}.")
        break
    elif respuesta == 'mayor':
        limite_inferior = intento + 1
    elif respuesta == 'menor':
        limite_superior = intento - 1
    
    # Si los límites se cruzan, el número no puede ser adivinado.
    if limite_inferior > limite_superior:
        print("Algo no concuerda con las respuestas. No se puede adivinar el número bajo estas condiciones.")
        break
else:
    # El bucle 'for' concluyó sin adivinar el número.
    print("No fue posible adivinar el número en los intentos dados.")