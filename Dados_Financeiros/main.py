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

    #    Lista = ['TIMB','VIVT3.SA','PETR3.SA','BBAS3.SA','CMIG4.SA','VALE3.SA']
    #    Lista_Aux = ['TIM','VIVO','PETROBRAS','BBRASIL','CEMIG','VALE']

    #    Lista = ['ABEV3.SA','ODPV3.SA','VIVT3.SA','PETR3.SA','BBAS3.SA','BOVA11.SA']
    #    Lista_Aux = ['AMBEV','ODONTOPREV','VIVO','PETROBRAS','BBRASIL','BOVA']
        
    a = AcoesGeral(Lista,Lista_Aux)
    a.acoesGeral()