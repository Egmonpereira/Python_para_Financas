class Exercicio07(object):
    def __init__(self, Nome, N1, N2):
        self.Nome = Nome
        self.N1 = N1
        self.N2 = N2

    def aluno01(self):
        print()
        print('Aluno: ',self.Nome)
        print('Notas: %.2f e %.2f' %(self.N1,self.N2))
        if (self.N1 + self.N2)/2 >= 60:
            print('Aprovado com média ',(self.N1 + self.N2)/2)
        else:
            print('Reprovado com média ',(self.N1 + self.N2)/2)