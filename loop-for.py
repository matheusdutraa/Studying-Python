# Criando uma tupla e imprimindo cada um de seus valores

tp = (2, 5, 7, 8, 9)

for i in tp:
    print(i)

# Criando uma lista e imprimindo cada um de seus valores
print("\b")

listaDAM = ["Faca", "Segundo Andar", "Remédio"]

for lis in listaDAM:
    print(lis)

# Imprimindo os valores no intervalo de 0 e 5
print("\b")

for contador in range(0, 5):
    print(contador)

# Imprimindo na tela os números pares
print("\b")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for num in lista:
    if num % 2 == 0:
        print(num)

# Imprimindo números impares na tela
print("\b")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for nume in lista:
    if nume % 2 == 1:
        print(nume)

# Listando os números no intervalo entre 0 e 101, com inceremento em 2
print("\b")

for i in range(0, 101, 2):
    print(i)

# Strings também são sequências
print("\b")

for caracter in 'Python é a linguagem mais divertida!':
    print(caracter)
