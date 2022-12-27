import random

class Exercicio01(object):
    def __init__(self):
        pass

    def exe01(self):
        a = random.randint(1,100)#int(input('Digite um número inteiro: '))
        b = random.randint(1,100)#int(input('Digite um número inteiro: '))

        print(a,b)
        print('Adição: ', a + b)
        print('Subtração: ', a - b)
        print('Multiplicação: ', a * b)
        print('Divisão: ', a / b)
        
    def viagem(self):
        print()
        tempo = 210#float(input('Tempo de viagem em minutos totais: '))
        veloc = 60#float(input('Velocidade média durante a viagem: '))
        consu = 12#float(input('Cosnumo médio durante a viagem: '))
        dista = tempo/60 * veloc
        print('Distância percorrida: ', dista,'Km')
        litro = dista / consu
        print('Velocidade Média: %2d km' %veloc)
        print('Tempo gasto na viagem %.2fh' %(tempo/60))
        print('Distância percorrida: %.2f km' %dista)
        print('Quantidade de litros gastos: %.2f Litros' %litro)

