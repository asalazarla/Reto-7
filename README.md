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



```python
```


```python
```


