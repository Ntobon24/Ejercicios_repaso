import random

filas = int(input("ingrese la cantidad de filas de la matriz: "))
columnas = int(input("ingrese la cantidad de columnas de la matriz: "))
range_max = int(input("ingrese el rango maximo de los numeros en la matriz: "))

m = [[random.randint(1,range_max) for j in range(columnas)] for i in range(filas)]

for f in m:
    print(f)
