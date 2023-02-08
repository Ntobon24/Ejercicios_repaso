import random

z = int(input("ingrese el la cantidad de numeros random que desea: "))

aleatorios = [random.randrange(0, 100, 2) for _ in range(z)]
print(aleatorios)
