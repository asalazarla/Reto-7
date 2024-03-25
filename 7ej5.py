# Solicitamos al usuario que ingrese un número natural n
n = int(input("Ingrese un número natural para calcular su factorial: "))

# Inicializamos la variable para almacenar el factorial
factorial = 1

# Verificamos que el número sea natural (mayor o igual a 0)
if n < 0:
    print("El número ingresado debe ser un número natural (mayor o igual a 0).")
else:
    # Calculamos el factorial con un ciclo for
    for i in range(1, n+1):
        factorial *= i
        # La palabra 'break' no se necesita realmente aquí, pero si quisiéramos
        # podríamos usarla para salir del bucle bajo alguna condición especial
        if False:  # Esto es solo un marcador de posición, no se ejecutará
            break

    # Imprimimos el resultado
    print(f"El factorial de {n} es {factorial}")