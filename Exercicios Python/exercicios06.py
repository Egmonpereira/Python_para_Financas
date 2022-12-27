import re

class Exercicio06(object):
    def __init__(self):
        pass

    def exe06(self):
        #Função search
        frase = 'Olá, meu número de telefone é (31)99728-4312'
        print(re.search('\(\d{2}\)\d{4,5}-\d{4}',frase))

        frase2 = 'A placa de carro que eu anotei durante o acidente foi FrT-1998'
        print(re.search('\w{3}-\d{4}',frase2))
        print(re.search('[A-Za-z]{3}-\d{4}',frase2))

        email = 'Entre em contato, meu email é egmon@ufmg.br'
        print(re.search('\w+@\w+\.\w+',email))

        #Função match
        frase3 = 'A placa de carro que eu anotei durante a batida foi FRT-1998'
        print(re.match('[A-Za-z]{3}-\d{4}',frase3))

        frase4 = 'FRT-1998 é a placa do carro'
        print(re.search('[A-Za-z]{3}-\d{4}',frase4))
        print(re.match('[A-Za-z]{3}-\d{4}',frase4))

        #Função findall
        frase5 = 'Meu número de telefone atual é (31)99728-4312. O número (56)1111-1111 é o antigo'
        print(re.search('\(\d{2}\)\d{4,5}-\d{4}',frase5))        
        print(re.findall('\(\d{2}\)\d{4,5}-\d{4}',frase5))        

        emails = '''Nome: Teste 1
        email: teste1@teste.com
        Nome: Teste 2
        email: teste2@teste.com
        Nome: Teste 3
        email: teste3@teste.com.br
        '''
        print(re.findall('\w+@\w+\.\w*',emails))
