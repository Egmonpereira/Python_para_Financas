class Exercicio04(object):
    def __init__(self):
        pass

    def exe04(self):
        def String(s):
            return s

        s = 'Ana'#input('Digite uma palavra: ')
        print(String(s))

        def Float(f):
            return f

        try:
            f = 2.58#float(input('Digite um número: '))

            print(Float(f))
        except:
            print('erro')
