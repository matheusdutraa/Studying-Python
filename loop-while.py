# Usando loop while para imprimir valores de 0 a 9

counter = 0

while counter < 10:
    print(counter)
    counter += 1

# Também da de usar else para encerrar o while
print("\b")

x = 0

while x < 10:
    print('O valor de x nesta iteração é: ', x)
    print(' x ainda é menor que 10, somando 1 ao x')

    x += 1

else:
    print('Loop Concluído!')

# Pass, Break, Continue
print("\b")

contador = 0

while contador < 100:
    if contador == 4:
        break
    else:
        pass
    print(contador)
    contador += 1

print("\b")

for verificador in 'Python':
    if verificador == 'h':
        continue
    print(verificador)

# While e for juntos
print("\b")

for i in range(2, 30):

    j = 2
    contado = 0

    while j < i:
        if i % j == 0:
            contado = 1
            j += 1
        else:
            j += 1
    if contado == 0:
        print(str(i) + " é um número primo")
        contado = 0
    else:
        contado = 0








