valor = int(input("ingrese el numero el cual desea conocer su factorial: "))

def factorial(numero):
    if numero <= 0:
        return 1
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial


def factorial_(numero):
    if numero <= 1:
        return 1
    return numero * factorial(numero-1)

resultado= factorial(valor)
print(f"El factorial de {valor} es {resultado}")