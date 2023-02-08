lista = [2, 4, 7, 8, 5, 4, 4, 3, 8, 10, 16, 7]
tamano = len(lista)
lista_sumada = 0

for i in range(tamano):
    lista_sumada = sum(lista)

media = lista_sumada/tamano

print(f"la media de la lista es: {media}")
