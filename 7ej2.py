# Se solicita el ingreso de un número natural n mayor o igual a 2
n = int(input("Ingrese un número natural n (mayor o igual a 2): "))

# Se verifica que n sea mayor o igual a 2
if n >= 2:
    # Si n es impar, restamos 1 para empezar con el par más cercano
    if n % 2 != 0:
        n -= 1
    
    # Inicia un ciclo while, que irá desde n hasta 2
    while n >= 2:
        # Imprimimos el número par
        print(n)
        # Se ordena de dos en dos para seguir con los pares
        n -= 2
else:
    print("El número ingresado no es mayor o igual a 2.")
