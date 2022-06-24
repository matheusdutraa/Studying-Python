# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numeros)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
print("\n")

objetos = ["Vagabond", "Berserk", "Chainsaw Man", "Monster", "Mushoku Tensei"]

print(objetos)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
print("\n")


first = "Elon"
second = "Musk"
third = first + " " + second

print(third)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
print("\n")

tupla1 = (1, 2, 3, 4, 5, 4)

print(tupla1.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
print("\n")

dicio = {}

print(dicio)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
print("\n")

dicionario1 = {"Matheus": 17, "Jefferson": 32, "Guanabara": 41}

print(dicionario1)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
print("\n")

dicionario1["Marcos"] = 36

print(dicionario1)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos.
# Imprima o dicionário na tela.
print("\n")

diciolista = {"Velhos": [66, 48, 51, 60], "Comida": "Boa", "Novos": [11, 16, 19, 21]}

print(diciolista)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string,
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
print("\n")

listamaluca = ["Normal", ("Fazenda Feliz", 8), {"Colheita Verde":9, "Dragon City":6}, 8.7]

print(listamaluca)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
print("\n")

frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

print(frase[0:18])

