# Abrindo o arquivo para leitura
arqu1 = open("Arquivo1.txt", "r")  # Repare no "r"

# lendo o arquivo
print(arqu1.read())


# Contar o número de caracteres (não acho que isso vá a ser útil, mas ai está_)
print(arqu1.tell())

# Retornar para o Inicio do Arquivo
print(arqu1.seek(0, 0))

# Ler os primeiros 10 caracteres
print(arqu1.read(10))

# ------------------ Gravando Arquivos ------------------------

# Abrindo arquivo para gravação
arqu2 = open("arquivo2.txt", "w")  # Repare no "w"

# Quando o arquivo é aberto apenas para gravação, não é possivel fazer leitura
# print(arqu2.read()) <-- Vai dar erro

# Gravando Arquivo
arqu2.write("Gravando Algo no arquivo TXT super legal minecraft")

# Fechando o arquivo
arqu2.close()


# Lendo o arquivo gravado
arqu2 = open("arquivo2.txt", "r")

print(arqu2.read())

# Acrescentando conteúdo
arqu2 = open("arquivo2.txt", "a")  # Repare no "a"

arqu2.write(" Acrescentando conteudo")

arqu2.close()

arqu2 = open("arquivo2.txt", "r")

print(arqu2.read())

# Retornando no início do arquivo para leitura

arqu2.seek(0, 0)

print(arqu2.read())

# ------------------ Automatizando processo de gravação ------------------------

fileName = input("Digite o nome do arquivo: ")

fileName += ".txt"

arqu3 = open(fileName, 'w')

arqu3.write("Incluindo Texto no arquivo Criado")

arqu3.close()

arqu3 = open(fileName, 'r')

print(arqu3.read())
