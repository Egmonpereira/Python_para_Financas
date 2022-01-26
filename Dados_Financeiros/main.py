#br.financas.yahoo.com

import os 

from acoesgol import AcoesGol 
from acoesgeral import AcoesGeral
    
if __name__ == '__main__':
    os.system('clear')
    
    s = 'n'#input('Entrar com dados? S/N: ').lower()
    if s == 's':
        n = 1
        Lista = []
        while n != '':
            print('Entre com o código das ações:')
            n = input('Código: ')
            Lista.append(n)
            os.system('clear')
            print(Lista)
        os.system('clear')
        Lista.pop()        
        print(Lista)

        n = 1
        Lista_Aux = []
        s = input('Deseja renomear como os código aparecerão nas colunas? S/N: ').lower()
        if s == 's':
            for i in Lista:
                print('\nRenomei o Código',i,': ',end='')
                n = input()
                Lista_Aux.append(n)
                os.system('clear')
                for j in range(len(Lista_Aux)):
                    print(Lista[j],':',Lista_Aux[j],', ',end='')
            os.system('clear')
        else:
            Lista_Aux = Lista
        print('\n',Lista_Aux)
    else:
        Lista = ['GOLL4.SA','CVCB3.SA','WEGE3.SA','MGLU3.SA','TOTS3.SA','BOVA11.SA']
        Lista_Aux = ['GOL','CVC','WEGE','MAGALU','TOTS','BOVA']
        Lista2 = ['ABEV3.SA','ODPV3.SA','TIMB','VIVT3.SA','PETR3.SA','BBAS3.SA','CMIG4.SA','VALE3.SA','BOVA11.SA']
        Lista_Aux2 = ['AMBEV','ODONTOPREV','TIM','VIVO','PETROBRAS','BBRASIL','CEMIG','VALE','BOVA']
        Lista3 = ['AMER3.SA','MGLU3.SA']
        Lista_Aux3 = ['AMERICANAS','MAGALU']
    
    a = AcoesGeral(Lista2,Lista_Aux2)
    a.acoesGeral()