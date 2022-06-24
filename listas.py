# Lista de 1 elemento

lista = ["Arroz, Feijão, Macarrão"]

print(lista)

# Lista de 4 elementos

lista2 = ["Leite", 64, "laranja", 11]

print("\n")

print(lista2)

a = lista2[1]

print(a)

# Lista dentro de lista

lista3 = [["Um", "Dois", "Zero"], ["Cinza", 2], ["Marrom", "Sorvete", "Frio"]]

b =  lista3[2][1]

print(b)

c = lista3[0]

print(c)

# Juntando listas

print("\n")

lista23 = lista2 + lista3

print(lista23)

# Procurando algo na lista

print("\n")

print(64 in lista2)


# Adicionar elemento

lista2.append("Feijão")

print(lista2)

# Criando lista vazia

lista0 = []

# Copiar valores de uma lista para outra

for item in lista2:
    lista0.append(item)

print(lista0)

# Reverter lista

lista0.reverse()

print(lista0)

# Ordenar lista

x = [0, 4, 3, 5, 1, 2]

x.sort()

print(x)
