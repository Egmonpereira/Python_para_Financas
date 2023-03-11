from clean import Clean

class Dados(object):
    def __init__(self,s):
        self.s = s 

    def dados(self):
        if self.s == 'n':
            Lista = ['GOLL4.SA','CVCB3.SA','WEGE3.SA','MGLU3.SA','TOTS3.SA','BOVA11.SA']
            Lista_Aux = ['GOL','CVC','WEGE','MAGALU','TOTS','BOVA']
            print(Lista_Aux)
            name = 'GOL'
            Sai = ['WEGE','MAGALU','TOTS','BOVA']

            '''
            Lista = []
            n = ''
            while n != '':
                print('Entre com o código das ações:')
                n = input('Código: ').upper()
                Lista.append(n)
                Clean.clean('self')
                print(['GOLL4.SA','CVCB3.SA','WEGE3.SA','MGLU3.SA','TOTS3.SA','BOVA11.SA'])
                print('Tecle ENTER para encerrar')
        
                print('Lista de Ações = ',Lista)
                Clean.clean('self')
            
            Lista.pop()        
            print(Lista)

            n = 1
            Lista_Aux = []
            s = input('Deseja renomear como os código aparecerão nas colunas? S/N: ').lower()
            if s == 's':
                for i in Lista:
                    print('\nRenomei o Código',i,': ',end='')
                    n = input().upper()
                    Lista_Aux.append(n)
                    Clean.clean('self')
                    
                    for j in range(len(Lista_Aux)):
                        print(Lista[j],':',Lista_Aux[j],', ',end='')
                Clean.clean('self')

            else:
                Lista_Aux = Lista
            print('\n',Lista_Aux)
            
            
            Clean.clean('self')
            
            print(Lista)
            for i in Lista:
                print(i,end=' ')
                n = input('Sai? S/N: ').lower()
                if n == 's':
                    Lista.remove(i)
            print(Lista)
            '''            
        
        else:
            print('Escolha uma Lista:')
            print('Lista 1 = ',['GOL','CVC','WEGE','MAGALU','TOTS','BOVA'])
            print('Lista 2 = ',['TIM','VIVO','PETROBRAS','BBRASIL','CEMIG','VALE'])
            print('Lista 3 = ',['AMBEV','ODONTOPREV','VIVO','PETROBRAS','BBRASIL','BOVA'])
            print('Lista 4 = ',['AAPL.SA','AMZN.SA','GOOG.SA','META.SA','NFLX.SA','TSLA.SA'],'\n')

            op = input('Lista 1 - 2 - 3 - 4: ').lower()

            if op == '1':
                Lista = ['GOLL4.SA','CVCB3.SA','WEGE3.SA','MGLU3.SA','TOTS3.SA','BOVA11.SA']
                Lista_Aux = ['GOL','CVC','WEGE','MAGALU','TOTS','BOVA']
                print(Lista_Aux)
                name = input('Nome da Ação a ser analisada: ').upper()
                Sai = ['WEGE','MAGALU','TOTS','BOVA']
            elif op == '2':
                Lista = ['TIMB','VIVT3.SA','PETR3.SA','BBAS3.SA','CMIG4.SA','VALE3.SA']
                Lista_Aux = ['TIM','VIVO','PETROBRAS','BBRASIL','CEMIG','VALE']
                print(Lista_Aux)
                name = input('Nome da Ação a ser analisada: ').upper()
                Sai = ['PETROBRAS','BBRASIL','CEMIG','VALE']
            elif op == '3':
                Lista = ['ABEV3.SA','ODPV3.SA','VIVT3.SA','PETR3.SA','BBAS3.SA','BOVA11.SA']
                Lista_Aux = ['AMBEV','ODONTOPREV','VIVO','PETROBRAS','BBRASIL','BOVA']
                print(Lista_Aux)
                name = input('Nome da Ação a ser analisada: ').upper()
                Sai = ['VIVO','PETROBRAS','BBRASIL','BOVA']
            elif op == '4':
                Lista = ['AAPL.SA','AMZN.SA','GOOG.SA','META.SA','NFLX.SA','TSLA.SA']
                Lista_Aux = ['AAPL','AMZN','GOOG','META','NFLX','TSLA']
                print(Lista_Aux)
                name = input('Nome da Ação a ser analisada: ').upper()
                Sai = ['GOOG','META','NFLX','TSLA']
            else:
                print('Opção inválida!')
    
            
        print('\nAções a serem analisadas = ', Lista_Aux)
        
        return Lista, Lista_Aux, name, Sai