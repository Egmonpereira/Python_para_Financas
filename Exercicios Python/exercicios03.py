import random, numpy

class Exercicio03(object):
    def __init__(self):
        pass

    def exe03(self):
        L = []
        for i in range(5):
            L.append(random.randint(0,1000))
        print()
        print(L)

        print("Soma de todos os números da Lista L = %d" %(sum(L)))

        dict = {}
        dict = {'Fabio': random.randint(0,100), 'Ana': random.randint(0,100), 'Tiago': random.randint(0,100)}
        print(dict)

        soma = 0
        for i in dict.values():
            soma += i
        print('Média das notas %.2f' %(soma/3))

        Matriz = numpy.array([[3, 4, 1],
                   [3, 1, 5]])

        soma = 0
        for i in Matriz:
            soma += sum(i)
        print('\nSoma da Matriz = %d' %soma)