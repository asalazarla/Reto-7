def es_primo(n):
    """
    Esta función verifica si un número n es primo.
    Retorna True si n es primo, de lo contrario retorna False.
    """
    # Los números menores de 2 no son primos
    if n < 2:
        return False
    # Verificamos si n tiene algún divisor además de 1 y él mismo
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Bucle para probar cada número en el rango del 1 al 100
print("Números primos del 1 al 100:")
for numero in range(1, 101):
    if es_primo(numero):
        print(numero, end=" ")
print()  # Añade un salto de línea al final