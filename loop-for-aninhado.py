# Loops aninhados

for i in range(0, 5):
    for a in range(0, 5):
        print(a)

# Oprando os valores de uma lista com loop for
print("\b")

listaA = [15, 46, 22, 52, 55, 11, 44, 61]

soma = 0

for i in listaA:
    double_i = i * 2
    soma += double_i

print(soma)

# Loops em lista de listas
print("\b")

listas = [[12, 33, 44], [1, 63, 12], [4, 8, 15]]

for valor in listas:
    print(valor)

# Contando conteúdo de uma lista
print("\b")

lista = [1, 2, 5, 7, 3, 6, 4]

count = 0

for item in lista:
    count += 1

print(count)

# Contando o número de colunas
print("\b")

lst = [[1, 12, 2, 3], [4, 5, 15, 6], [7, 8, 15, 9], [42, 11, 22, 15]]

primeira_linha = lst[0]

count = 0

for column in primeira_linha:
    count += 1

print(count)

# Pesquisando em listas
print("\b")

listaB = [5, 6, 11, 12, 15, 16]
"""
# Loop através de lista
print("\b")

contador = 0

numer = int(input("Qual número você quer encontrar na lista?"))

for item in listaB:
    if item == numer:
        print("Número encontrado na lista, na posição: ", contador)
    else:
        print("Número não encontrado na posição: ", contador)

    contador += 1
"""

# Listando as chaves de um dicionario
print("\b")

dict = {'v1': 'Python', 'v2': 'Limoeiro', 'v3': 'Laranjal'}

for item in dict:
    print(item)

# Imprimindo chave e valor do dicionário. Usando o método items() para retornar os itens de um dicionário
print("\b")

for k, v in dict.items():
    print(k, v)

print("\b")

for k, v in dict.items():
    print(v)
