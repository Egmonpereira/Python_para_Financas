class Exercicio05(object):
    def __init__(self):
        pass

    def exe05(self):
        A = list()
        alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}
        for i in alunos.items():
            A.append(i)
            A.append('\n')

        with open('Alunos.txt', 'w') as Alunos:
            for i in range(len(A)):
                Alunos.writelines(str(A[i]))

        with open('Alunos.txt', 'r') as Alunos:
            for i in Alunos:
                print(i)
