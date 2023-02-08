import random

z = int(input("ingrese el la cantidad de numeros random que desea: "))
range_max = int(input("ingrese el rango max: "))

aleatorios = [random.randrange(0, range_max) for _ in range(z)]
print(aleatorios)
