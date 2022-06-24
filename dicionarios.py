# Isso é um dicionário

os_guri = {"Matheus":17, "Gabriel":18, "Thiago":17}

print(os_guri)

print("\nA idade do Matheus é:", os_guri["Matheus"], "Anos.")

# Adicionando conteúdo

os_guri["Guillermo"] = 17


print("\n", os_guri)
"""
# Apagando dicionario

os_guri.clear()

print(os_guri)

# Deletando o dicionario

del os_guri

print(os_guri) """

#

print(os_guri.items())

os_guri2 = {"Marco":16, "Henry":17}

os_guri.update(os_guri2)

print("\n", os_guri)

#

print("\n\n")

garrafa = {"13":"Python", "Third":['Leite', 'Roxo']}

print(garrafa)

print(garrafa['Third'][0].upper())


