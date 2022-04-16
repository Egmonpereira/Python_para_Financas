#br.financas.yahoo.com

import pandas as pd

from clean import Clean
from dados import Dados
from acoesgerais import AcoesGerais
from calculo_risco import Calculo_Risco
from alocacao_portifolio import Alocacao_Otimizacao
from alocacao_ativos import Alocacao_Ativos
from taxa_retorno_acoes import Taxa_Retorno_Acoes
from otimizacao_portifolio import Otimizacao_Portifolio
from capm import Capm

if __name__ == '__main__':
    Clean.clean('self')

    s = 'n'#input('Entrar com dados? S/N: ').lower()
    Lista, Lista_Aux, name, Sai = Dados(s).dados()

    try:       
        a = AcoesGerais(Lista,Lista_Aux)
        print("Executando Acoes Gerais:")
        #a.acoesGerais()
    except:
        print('Nenhuma Lista selecionada!')
    
    try:
        b = Taxa_Retorno_Acoes(Lista, Lista_Aux)
        print("\n\nExecutando Taxa Retorno Acoes:")
        #dataset = b.taxa_retorno_acoes()
    except:
        print('Nenhuma Taxa calculada')
    
    try:
        c = Calculo_Risco(name,Sai)
        print('\n\nExecutando Cálculo de Risco:')
        taxa_selic_historico = c.calculo_risco()
    except:
        print('Nenhum Risco calculado')
    
    try:
        #d = Alocacao_Ativos(dataset, 5000, 10)
        print('\n\nExecutando Alocacao e Otimizacao:')
        #acoes_pesos, soma_valor, dataset, desvio_padra_taxa_retorno, taxa_retorno_acum, sharpe_ratio_medio = d.alocacao_ativos()

        try:
            print('\nSharpe Ratio')
            execs = 1#int(input('Número de Execuções: '))
            #e = Alocacao_Otimizacao(pd.read_csv('acoesGerais.csv'), 5000, taxa_selic_historico.mean() / 100, execs)
            #melhor_sharpe_ratio, melhores_pesos, Lista_retorno_esperado, Lista_volatividade_esperada, Lista_sharpe_ratio, melhor_volatilidade, melhor_retorno = e.alocacao_portifolio()
        except:
            print('Número de Execuções deve ser um número inteiro! ')
            print('Serão ralizadas 10 execuções.')
            execs = 10
        
        '''Pesos = pd.DataFrame(melhores_pesos)
        Pesos.columns=['Pesos']
        print('\nMelhores Pesos:')
        print(Pesos)
        print('\nmelhor_volatilidade',melhor_volatilidade)
        print('\nmelhor_retorno',melhor_retorno)'''
    except:
        print('Nenhuma Alocação executada')
    
    try:
        f = Otimizacao_Portifolio(pd.read_csv('acoesGerais.csv'), 5000, taxa_selic_historico.mean() / 100)
        print('\nOtimizacao Portifolio')
        #f.otimizacao_portifolio()
    except:
        print('Nenhuma Otimização de Portifólio executada')

#    try:
    Capm = Capm(Lista_Aux)
    print('\nExecutando CAPM\n')
    Capm.capm()
#    except:
#        print('Nenhuma CAPM executada')