# Reto-7
Este repositorio desarrolla los ejercicios planteados en el reto 7 y los de la clase 10 enfocada en bucles.

## **Ejercicios de clase:**

1. Diseñe un algoritmo que involucre un ciclo y que nunca ingrese al ciclo.
   
```python
# Inicialización de la variable
condicion = False

# Ciclo while con una condición que nunca se cumple
while condicion:
    # Este bloque nunca se ejecutará
    pass

print("Este algoritmo nunca entra al ciclo.")
```

2. Diseñe un algoritmo que involucre un ciclo y que se ejecute indefinidamente.
```python
# Ciclo while con una condición siempre verdadera
while True:
    print("Este ciclo se ejecuta indefinidamente.")
    # Advertencia: Este es un ciclo infinito y deberá ser interrumpido manualmente.
```

3. Diseñe un algoritmo que pida un valor entero, y que siga leyendo valores enteros mientras que alguno de esos valores no represente el código ASCII de una letra mayúscula en el abc del inglés.
```python
# Ciclo while que se ejecuta hasta que se reciba un código ASCII de una letra mayúscula en inglés
while True:
    valor = int(input("Ingrese un valor entero: "))
    if 65 <= valor <= 90:
        # Si el valor está en el rango de letras mayúsculas, rompe el ciclo
        break
    else:
        print(f"El valor {valor} no es el código ASCII de una letra mayúscula en inglés.")

print(f"El valor {valor} representa una letra mayúscula en el abecedario inglés.")
```
_________________________________________________________________________________________________________________________________________________________

## **Ejercicios del reto:**
**NOTA:** Todos los códigos se encuentran debidamente documentados. :) 

1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
   
```python
# Inicialización de la variable que llevará la cuenta de los números
i = 1

# Ciclo while que se ejecutará mientras i sea menor o igual a 100
while i <= 100:
    # Se calcula el cuadrado del número actual
    cuadrado = i ** 2
    # Se imprime el número y su cuadrado
    print(f"El cuadrado de {i} es {cuadrado}")
    # Se actualiza el valor de i para la siguiente iteración
    i += 1
```

* A continuación su respectivo **diagrama de flujo** :
```mermaid
```
2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
   
```python
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
```

* A continuación su respectivo **diagrama de flujo** :
```mermaid

```

3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
   
```python
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
```

* A continuación su respectivo **diagrama de flujo** :
```mermaid
```

4. En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.

```python
# Datos iniciales
poblacion_a = 25e6  # 25 millones
poblacion_b = 18.9e6  # 18.9 millones
tasa_a = 0.02  # 2%
tasa_b = 0.03  # 3%
año = 2022  # Año inicial

# Ciclo while para calcular el crecimiento anual
while poblacion_b <= poblacion_a:
    # Crecimiento anual de la población
    poblacion_a += poblacion_a * tasa_a
    poblacion_b += poblacion_b * tasa_b
    # Incrementamos el año en cada iteración
    año += 1

# Al final del ciclo, se imprime el año en que la población de B supera a la de A
print("La población del país B superará a la del país A en el año", año)

```

5. Imprimir el factorial de un número natural n dado.
   
```python
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
```

6. Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.
   
```python
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
```

7. Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.
```python
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
```

8. Implementar el algoritmo que muestre los números primos del 1 al 100. **Nota:** use funciones.
   
```python
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
```

