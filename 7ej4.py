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

