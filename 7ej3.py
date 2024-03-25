# Se solicita el ingreso de un número natural n mayor o igual a 2
n = int(input("Ingrese un número natural n (mayor o igual a 2): "))

# Se verifica que n sea mayor o igual a 2
if n < 2:
    print("El número ingresado debe ser mayor o igual a 2.")
else:
    # Si n es impar, se resta 1 para empezar con el par más cercano que sea menor que n
    if n % 2 != 0:
        n -= 1

    # Inicia un ciclo while, que irá desde n hasta 2
    while n >= 2:
        # Se imprime el número par
        print(n)
        # Se ordena de dos en dos para seguir con los números pares
        n -= 2