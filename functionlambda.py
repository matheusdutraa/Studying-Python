# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e
# depois faça uma chamada à função para listar os números

import pandas as pd


def imprimirNpares(num, num2):
    while num <= num2:
        if num % 2 == 0:
            print(num, " eh par.")
        num += 1


imprimirNpares(1, 20)


# Exercício 2 - Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def caixaAlta(string):

    print(string.upper())


caixaAlta("Juggernaut")


# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e
# imprima a lista


def listal(list):
    list.append("Agua")
    list.append("Python")

    print(list)


lista = ["Laur", "Hipopotamo", "Relatividade", 18]

listal(lista)


# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def printNum(arg1, *lista):
    print(arg1)
    for i in lista:
        print(i)
    return


# Chamada à função
printNum(100)
printNum('A', 'B', 'C')

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2
# números como parâmetro e retornar a soma deles


def somar(num, num1):
    soma = num + num1
    print(soma)


somar(141, 515)

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2
# números como parâmetro e retornar a soma deles


def soma(arg1, arg2): return arg1 + arg2


print("A soma é : ", soma(452, 298))


# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0


def soma(arg1, arg2):
    total = arg1 + arg2
    print("Dentro da função o total é: ", total)
    return total


soma(10, 20)
print("Fora da função o total é: ", total)

# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!

"""
Celsius → Fahrenheit
Multiplicamos a temperatura em ºC por 1,8 e somamos 32 ao resultado.
"""

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print(list(Fahrenheit))


# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário

dic = {'k1': 'Natal', 'k2': 'Recife'}
dir(dic)

# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.

pd.__version__

dir(pd)

# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"


file_name = "binary.csv"


def retornaArq(file_name):
    df = pd.read_csv(file_name)
    return df.describe()


retornaArq(file_name)
