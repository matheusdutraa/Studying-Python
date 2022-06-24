
import math


def primeiraFunc(nome):
    print('Primeira Funcao, ola ' + nome)


print(primeiraFunc('Matheus'))


def segundaFunc(number, number2):
    print('Segunda Funcao, o numero eh ' + str(number))
    print('Segunda Funcao, o numero eh ' + str(number2))
    print('A soma eh ' + str(number + number2))


print(segundaFunc(10, 20))


def numerosPares(number):
    if number % 2 == 0:
        return 'O numero eh par'
    else:
        return 'O numero eh impar'


print(numerosPares(215))


def numeroPrimo(number):
    """Verificando se o número é primo"""

    if (number % 2) == 0 and number > 2:
        return "O número é par e não primo"
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if (number % i) == 0:
            return "Este número não é primo"
    return "Este número é primo"


print(numeroPrimo(119))


# Fazendo split dos dados

def split_string(text):
    return text.split(" ")


texto = "Como a democracia seria algo bom, se a maioria das pesoas não sabem nem o básico sobre política? "

print(split_string(texto))

token = split_string(texto)

print(token)
