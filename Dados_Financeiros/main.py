#br.financas.yahoo.com

import pandas

from datetime import date
from clean import Clean
from dados import Dados
from acoesgerais import AcoesGerais
from calculo_risco import Calculo_Risco
from alocacao_portifolio import Alocacao_Otimizacao
from alocacao_ativos import Alocacao_Ativos
from taxa_retorno_acoes import Taxa_Retorno_Acoes
from otimizacao_portifolio import Otimizacao_Portifolio
from capm import Capm
from simulacao_monte_carlo import Simulacao_Monte_Carlo
from arima import Arima
from facebookprophet import Fbprophet
from classifica_empresas import Classifica_Empresas

if __name__ == '__main__':
    Clean.clean('self')

    print('\n:::PRINCIPAL:::\n')
    s = 'n'#input('Entrar com dados? S/N: ').lower()
    Lista, Lista_Aux, name, Sai = Dados(s).dados()

    try:       
        a = AcoesGerais(Lista,Lista_Aux)
        with open('Data.txt', 'r') as Data:
            data = Data.read()
        if data != str(date.today()):
            with open('Data.txt', 'w') as Data:
                Data.write(str(date.today()))
            
            print("Importando dados das Acoes\n ",Lista_Aux)
            a.acoesGerais()
        else:
            print("Dados atualizados em",data)
    except Exception as erro:
        print(erro)
        print('Nenhuma Lista selecionada!')
    
    try:
        b = Taxa_Retorno_Acoes(Lista, Lista_Aux)
        print("\n\nExecutando Taxa Retorno Acoes:")
        dataset = b.taxa_retorno_acoes()
    except:
        print('Nenhuma Taxa calculada')
    
    try:
        c = Calculo_Risco(name,Sai)
        print('\n\nExecutando Cálculo de Risco:')
        taxa_selic_historico = c.calculo_risco()
    except:
        print('Nenhum Risco calculado')
    
    try:
        d = Alocacao_Ativos(dataset, 5000, 10)
        print('\n\nExecutando Alocacao e Otimizacao:')
        acoes_pesos, soma_valor, dataset, desvio_padra_taxa_retorno, taxa_retorno_acum, sharpe_ratio_medio = d.alocacao_ativos()

        try:
            print('\nSharpe Ratio')
            execs = 1#int(input('Número de Execuções: '))
            e = Alocacao_Otimizacao(pandas.read_csv('Bases_de_Dados/acoesGerais.csv'), 5000, taxa_selic_historico.mean() / 100, execs)
            melhor_sharpe_ratio, melhores_pesos, Lista_retorno_esperado, Lista_volatividade_esperada, Lista_sharpe_ratio, melhor_volatilidade, melhor_retorno = e.alocacao_portifolio()
        except:
            print('Número de Execuções deve ser um número inteiro! ')
            print('Serão ralizadas 10 execuções.')
            execs = 10
        
        Pesos = pandas.DataFrame(melhores_pesos)
        Pesos.columns=['Pesos']
        print('\nMelhores Pesos:')
        print(Pesos)
        print('\nmelhor_volatilidade',melhor_volatilidade)
        print('\nmelhor_retorno',melhor_retorno)
    except:
        print('Nenhuma Alocação executada')
    
    try:
        f = Otimizacao_Portifolio(pandas.read_csv('acoesGerais.csv'), 5000, taxa_selic_historico.mean() / 100)
        print('\nOtimizacao Portifolio').otimizacao_portifolio()
    except:
        print('\nNenhuma Otimização de Portifólio executada')

    try:
        Capm = Capm(Lista_Aux)
        print('\nExecutando CAPM\n')
        Capm.capm()
    except:
        print('Nenhuma CAPM executada')

    try:
        pass
        #S = Simulacao_Monte_Carlo(Lista, Lista_Aux, name).smc()
    except Exception as erro:
        print(erro)
        
    try:
        pass
        #A = Arima(Lista, Lista_Aux, name, Sai).arima()
    except Exception as erro:
        print(erro)

    try:
        F = Fbprophet(Lista, Lista_Aux, name, Sai).facebookprophet()
    except Exception as erro:
        print(erro)

    try:
        C = Classifica_Empresas().classifica_empresas()
    except Exception as erro:
        print(erro)