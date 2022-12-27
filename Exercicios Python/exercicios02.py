import random

class Exercicio02(object):
    def __init__(self):
        pass

    def exe02(self):
        try:
            i = random.randint(0,120)#int(input('\nDigite sua idade: '))
            print('Idade: %d anos' %i)
            if i < 0:
                print('Idade deve ser maior ou igual a Zero!')
                i = int(input('\nDigite sua idade: '))
                if i < 0:
                    print('Idade inválida!\nEncerrando o Programa')

            if i >= 0 and i < 13:
                j = 1
                print('Criança')
            elif i >= 12 and i < 18:
                j = 1
                print('Adolescente')
            elif i > 18:
                j = 1
                print('Adulto')

        except:
            print('Idade inválida!')
            s = input('Tentar novamente? S/N: ').upper()
            if s == 'S':
                Exercicio02().exe02()
            else:
                print('\nPrograma encerrando!')
    