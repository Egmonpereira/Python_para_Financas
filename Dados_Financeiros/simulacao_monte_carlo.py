import pandas
import numpy
import random

from scipy import stats
from pandas_datareader import data 
from sklearn.metrics import mean_absolute_error
from graficos import Grafico_smc

class Simulacao_Monte_Carlo(object):
    def __init__(self,Lista,Lista_Aux, name):
        self.Lista_Aux = Lista_Aux
        self.Lista = Lista
        self.name = name
    
    def previsao(dataset, ativo, dias_frente, simulacoes):
        print('\n:::SIMULAÇÃO MONTE CARLO:::\n')
        dataset = dataset.copy()
        dataset = pandas.DataFrame(dataset[ativo])
        
        dataset_normalizado = dataset.copy()
        for i in dataset:
            dataset_normalizado[i] = dataset[i] / dataset[i][0]

        dataset_taxa_retorno = numpy.log(1 + dataset_normalizado.pct_change())
        dataset_taxa_retorno.fillna(0, inplace=True)

        #Movimento Browniano para modelar r
        #Cálculo do drift - direção que as taxas de retorno tiveram no passado
        media = dataset_taxa_retorno.mean()
        variancia = dataset_taxa_retorno.var()

        drift = media - (0.5 * variancia)

        desvio_padrao = dataset_taxa_retorno.std()
        Z = stats.norm.ppf(numpy.random.rand(dias_frente, simulacoes))

        #Cálculo do retorno diário r
        retorno_diario = numpy.exp(drift.values + desvio_padrao.values * Z)

        #Previsões dos preços futuros
        previsoes = numpy.zeros_like(retorno_diario)
        previsoes[0] = dataset.iloc[-1]
        for dia in range(1, dias_frente):
            previsoes[dia] = previsoes[dia - 1] * retorno_diario[dia]

        return previsoes.T, Z

    
    def executa(dataset, Z, previsoes, Aux, Temp, dias_frente, i):   

        dataset_acao = data.DataReader(name=Temp[i], data_source='yahoo', start='2020-11-04')['Close']
        dataset_acao.to_csv('acao_teste.csv')
        dataset_acao = pandas.read_csv('acao_teste.csv')

        simulacao1 = previsoes[i][0:len(dataset_acao)]
        #print(dataset_acao[0:50]['Close'] - simulacao1)
        #print('\nErro médio em Reais entre a simulação e o valor real: ',',numpy.sum(abs(dataset_acao[0:50]['Close'] - simulacao1)) / len(simulacao1))
        print('\nErro médio em Reais entre a simulação e o valor real: R$ %.2f' %mean_absolute_error(dataset_acao[0:dias_frente]['Close'], simulacao1),'\n')
        
        erros = []
        print('Erro: ')
        for i in range(len(previsoes)):
            simulacao = previsoes[i][0:dias_frente]
            erros.append(mean_absolute_error(dataset_acao[0:dias_frente]['Close'], simulacao))
            print(i,'R$%.02f' %erros[i])
        for i in range(len(Aux)):
            print('\n',Aux[i])
            print('Menor Erro: R$%.02f' %min(erros))
            print('Maior Erro: R$%.02f' %max(erros))

        #Grafico_smc(dataset, Z, previsoes, 'self', Aux[i]).grafico_previsoes()

        #Grafico_smc(dataset, Z, previsoes, dataset_acao[0:dias_frente]['Close'], Aux[i]).grafico_simulacao()
        
    def smc(self):
        dataset = pandas.read_csv('acoesGerais.csv')

        t = 's'#input('Escolha a Ação a ser projetada sua previsão? ').lower()
        #Previsões para os próximos d dias a frente
        dias_frente = 300#int(input('Quantos dias a frente você deseja fazer a previsão? '))
        simulacoes = 10#int(input('Quantidade de Simulações: '))

        Aux = []
        Temp= []
        if t == 's':
            for i, j in zip(self.Lista_Aux, self.Lista):
                print('Inserir',i,'S/N? ',end='')
                s = 'n'#input().lower()
                if s == 's':
                    Aux.append(i)
                    Temp.append(j)
                    #Aux.append('PETROBRAS')
                    #Temp.append('PETR3.SA')
                    break
            if len(Aux) == 0:
                aux = random.randint(1,len(self.Lista_Aux) - 1)
                Aux.append(self.Lista_Aux[aux])
                Temp.append(self.Lista[aux])
                print('\nA Ação',Aux[0],'foi adicionada aleatoriamente.')
            else:
                print('\nA Ação',Aux[0],'foi a escolhida')

            previsoes, Z = Simulacao_Monte_Carlo.previsao(dataset, self.name, dias_frente, simulacoes)
            Simulacao_Monte_Carlo.executa(dataset, Z, previsoes, Aux, Temp, dias_frente, 0)
        else:
            
            for i, j in zip(self.Lista_Aux,self.Lista):
                Aux.append(i)
                Temp.append(j)


            for i in range(len(len(Aux))):
                previsoes, Z = Simulacao_Monte_Carlo.previsao(dataset, self.name, dias_frente, simulacoes)
                Simulacao_Monte_Carlo.executa(dataset, Z, previsoes, Aux, Temp, dias_frente, i)

        try:
            #Grafico_smc(dataset, 'self', 'self', 'self', str(Aux[0])).grafico_smc()
            pass
        except Exception as erro:
            print(erro)

