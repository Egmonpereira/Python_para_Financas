#br.financas.yahoo.com

import pandas
import time

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
from agrupamento_empresas import Agrupamento_Empresas
from analise_sentimentos import Analise_Sentimentos

if __name__ == '__main__':
    inicio = time.time()
    Clean.clean('self')

    print('\n:::PRINCIPAL:::\n')
    try:       
        with open('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/Data.txt', 'r') as Data:
            data = Data.read()
        if data != str(date.today()):
            #s = 's'#input('Entrar com dados? S/N: ').lower()
            Lista, Lista_Aux, name, Sai = Dados('s').dados()
            a = AcoesGerais(Lista,Lista_Aux)
            with open('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/Data.txt', 'w') as Data:
                Data.write(str(date.today()))
            print("Importando dados das Acoes\n ",Lista_Aux)
        else:
            Lista, Lista_Aux, name, Sai = Dados('n').dados()
            print("Dados importados em",data)
    except Exception as erro:
        print(erro)
        print('Nenhuma Lista selecionada!')
    
    try:
        print('\nTaxa de Retorno de Ações')
        b = Taxa_Retorno_Acoes(Lista, Lista_Aux)
        dataset = b.taxa_retorno_acoes()
    except:
        print('Nenhuma Taxa calculada')
    
    try:
        print('\nCálculo de Risco')
        c = Calculo_Risco(name,Sai)
        taxa_selic_historico = c.calculo_risco()
    except:
        print('Nenhum Risco calculado')
    
    try:
        print('\nAlocação de Ativos')
        d = Alocacao_Ativos(dataset, 5000, 10)
        acoes_pesos, soma_valor, dataset, desvio_padra_taxa_retorno, taxa_retorno_acum, sharpe_ratio_medio = d.alocacao_ativos()

        try:
            print('\nSharpe Ratio')
            execs = 30#int(input('Número de Execuções: '))
            e = Alocacao_Otimizacao(pandas.read_csv('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv'), 5000, taxa_selic_historico.mean() / 100, execs)
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
        print('\nOtimização de Portifólio')
        f = Otimizacao_Portifolio(pandas.read_csv('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv'), 5000, taxa_selic_historico.mean() / 100)
        print('\nOtimizacao Portifolio').otimizacao_portifolio()
    except:
        print('\nNenhuma Otimização de Portifólio executada')

    try:
        print('\nCAPM')
        Capm(Lista_Aux).capm()
    except:
        print('Nenhuma CAPM executada')

    try:
        print('\nSimulação de Monte Carlo')
        S = Simulacao_Monte_Carlo(Lista, Lista_Aux, name).smc()
    except Exception as erro:
        print(erro)
        
    try:
        print('\nArima')
        A = Arima(Lista, Lista_Aux, name, Sai).arima()
    except Exception as erro:
        print(erro)

    try:
        print('\nFaceBook Prophet')
        F = Fbprophet(Lista, Lista_Aux, name, Sai).facebookprophet()
    except Exception as erro:
        print(erro)

    try:
        print('\nClassificação das Empresas')
        C = Classifica_Empresas().classifica_empresas()
    except Exception as erro:
        print(erro)

    try:
        print('\nAgrupamento de Empresas')
        A = Agrupamento_Empresas().agrupamento_empresas()
    except Exception as erro:
        print(erro)

    try:
        print('\nAnálise de Sentimentos')
        A = Analise_Sentimentos().analise_sentimentos()
    except Exception as erro:
        print(erro)
    fim = time.time()

    with open('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/tempoExecucao.txt', 'w') as t:
        t.write(str('Tempo: %0.2f' %((fim - inicio)/60)))