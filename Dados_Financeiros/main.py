#br.financas.yahoo.com

import os 
import pandas as pd

from acoesgerais import AcoesGerais
from calculo_risco import Calculo_Risco
from alocacao_portifolio import Alocacao_Otimizacao
from alocacao_ativos import Alocacao_Ativos
from taxa_retorno_acoes import Taxa_Retorno_Acoes
from otimizacao_portifolio import Otimizacao_Portifolio
    
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
        name = 'GOL'
        Sai = ['WEGE','MAGALU','TOTS','BOVA']

#        Lista = ['TIMB','VIVT3.SA','PETR3.SA','BBAS3.SA','CMIG4.SA','VALE3.SA']
#        Lista_Aux = ['TIM','VIVO','PETROBRAS','BBRASIL','CEMIG','VALE']
#        name = 'TIM'
#        Sai = ['PETROBRAS','BBRASIL','CEMIG','VALE']

    #    Lista = ['ABEV3.SA','ODPV3.SA','VIVT3.SA','PETR3.SA','BBAS3.SA','BOVA11.SA']
    #    Lista_Aux = ['AMBEV','ODONTOPREV','VIVO','PETROBRAS','BBRASIL','BOVA']
    #    name = 'AMBEV'
    #    Sai = ['VIVO','PETROBRAS','BBRASIL','BOVA']
        
    print("Executando Acoes Gerais:")
    a = AcoesGerais(Lista,Lista_Aux)
    a.acoesGerais()
    
    print("\n\nExecutando Taxa Retorno Acoes:")
    b = Taxa_Retorno_Acoes(Lista, Lista_Aux)
    dataset = b.taxa_retorno_acoes()
    
    print('\n\nExecutando Cálculo de Risco:')
    c = Calculo_Risco(name,Sai)
    taxa_selic_historico = c.calculo_risco()
    
    print('\n\nExecutando Alocacao e Otimizacao:')
    print('\nAlocação de Ativos')
    d = Alocacao_Ativos(dataset, 5000, 10)
    acoes_pesos, soma_valor, dataset, datas, desvio_padra_taxa_retorno, taxa_retorno_acum, sharpe_ratio_medio = d.alocacao_ativos()
    print('\nacoes_pesos\n',acoes_pesos)
    print('\nsoma_valor:',soma_valor)
    print('\ndataset\n',dataset)
    print('\ndatas\n',datas)
    print('\ndesvio_padra_taxa_retorno:',desvio_padra_taxa_retorno)
    print('\ntaxa_retorno_acum:',taxa_retorno_acum)
    print('\nsharpe_ratio_medio:',sharpe_ratio_medio)
    
    print('\nSharpe Ratio')
    e = Alocacao_Otimizacao(pd.read_csv('acoesGerais.csv'), 5000, taxa_selic_historico.mean() / 100, 1)
    melhor_sharpe_ratio, melhores_pesos, Lista_retorno_esperado, Lista_volatividade_esperada, Lista_sharpe_ratio, melhor_volatilidade, melhor_retorno = e.alocacao_portifolio()
    print(melhor_sharpe_ratio)
    
    Pesos = pd.DataFrame(melhores_pesos)
    Pesos.columns=['Pesos']
    print('\nMelhores Pesos:')
    print(Pesos)
    print('\nmelhor_volatilidade',melhor_volatilidade)
    print('\nmelhor_retorno',melhor_retorno)
    
    print('\nOtimizacao Portifolio\n')
    f = Otimizacao_Portifolio(pd.read_csv('acoesGerais.csv'), 5000, taxa_selic_historico.mean() / 100)
    f.otimizacao_portifolio()
