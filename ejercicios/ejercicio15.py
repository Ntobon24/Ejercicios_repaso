texto = input("Ingrese la palabra que desea saber si es palindromo: ")

igual = 0
auxiliar = 0

for indice in reversed(range(0, len(texto))):
  if texto[indice] == texto[auxiliar]:
    igual += 1
    auxiliar += 1

if len(texto) == igual:
  print("El texto es palindromo!")
else:
  print("El texto no es palindromo!")