""" Litas para armazenar nome de alunos, e respectivamente suas classes, e também seus cursos.
 Note que o número representado pelo aluno também deve ser o mesmo representando para o própio curso e classe do própio..
 Tudo usando algum método para cadastra """

alunos = []

classes = []

cursos = []

switch = 1

while switch:

    escolha = int(input("Qual o seu desejo? \n"
          "1 - Cadastrar Aluno \n"
          "2 - Cadastrar Classe \n"
          "3 - Cadastrar Curso \n"
          "4 - Listar Aluno(s) \n"
          "5 - Listar Classe(s) \n"
          "6 - Listar Curso(s) \n"
          "7 - Remover Aluno \n"
          "8 - Remover Classe \n"
          "9 - Remover Curso \n"
          "10 - Sair \n"))

    if escolha == 1:

          al = str(input("Qual o nome do aluno que deseja cadastrar? \n"))
          alunos.append(al)
          print("Cadastrado com sucesso! \n")

    elif escolha == 2:

          cl = str(input("Qual o nome da classe que deseja cadastrar? \n"))
          classes.append(cl)
          print("Cadastrado com sucesso! \n")

    elif escolha == 3:

          cu = str(input("Qual o nome do curso que deseja cadastrar? \n"))
          cursos.append(cu)
          print("Cadastrado com sucesso! \n")

    elif escolha == 4:

          print(alunos)

    elif escolha == 5:

          print(classes)

    elif escolha == 6:

          print(cursos)

    elif escolha == 7:

          ra = str(input("Qual o nome do aluno que deseja remover? \n"))
          alunos.remove(ra)
          print("Removido com sucesso! \n")

    elif escolha == 8:

          rc = str(input("Qual o nome da classe que deseja remover? \n"))
          classes.remove(rc)
          print("Removido com sucesso! \n")

    elif escolha == 9:

          rcs = str(input("Qual o nome do curso que deseja remover? \n"))
          cursos.remove(rcs)
          print("Removido com sucesso! \n")

    elif escolha == 10:

          switch = 0








