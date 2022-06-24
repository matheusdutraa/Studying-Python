opcao = int(input("Selecione o número da operação desejada"
                  "\n1 - Soma"
                  "\n2 - Subtração"
                  "\n3 - Multiplicação"
                  "\n4 - Divisão\n"))

if(opcao == 1) or (opcao == 2) or (opcao == 3) or (opcao == 4):
    num = int(input("\nDigitre o primeiro número: "))
    num1 = int(input("\nDigite o segundo número: "))
    soma = 0

else:
    print("Opção Inválida!")
    exit()

if opcao == 1:
    soma = num + num1
    print("\n", num, " + ", num1, " = ", soma)

elif opcao == 2:
    soma = num - num1
    print("\n", num, " - ", num1, " = ", soma)

elif opcao == 3:
    soma = num * num1
    print("\n", num, " * ", num1, " = ", soma)

elif opcao == 4:
    soma = num / num1

    print("\n", num, " / ", num1, " = ", soma)
