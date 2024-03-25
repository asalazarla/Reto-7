# Solicitamos al usuario que ingrese un número entre 2 y 50
numero = int(input("Ingrese un número entre 2 y 50: "))

# Verificamos que el número esté en el rango permitido
if 2 <= numero <= 50:
    print(f"Los divisores de {numero} son: ", end="")
    # Utilizamos un ciclo for para encontrar e imprimir los divisores
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i, end=" ")
    print()  # Para añadir una nueva línea después de la lista de divisores
else:
    print("Número fuera de rango. Por favor ingrese un número entre 2 y 50.")