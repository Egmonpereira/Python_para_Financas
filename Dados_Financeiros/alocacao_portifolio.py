import sys
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import time
from alocacao_ativos import Alocacao_Ativos
from graficos import Portifolio

class Alocacao_Otimizacao(object):
    def __init__(self,dataset, dinheiro_total, sem_risco, repeticoes, seed = 0, melhores_pesos = []):
        self.dataset = dataset
        self.dinheiro_total = dinheiro_total
        self.sem_risco = sem_risco
        self.repeticoes = repeticoes
        self.seed = seed
        self.melhores_pesos = melhores_pesos
    
        
    def alocacao_portifolio(self):
        print('\n:::APENAS CHAMA ALOCAÇÃO PORTIFOLIO:::\n')
        ini = time.time()    
        dataset = self.dataset.copy()
        dataset_original = self.dataset.copy()
        colunas = dataset.columns[1:]
        Lista_retorno_esperado = []
        Lista_volatividade_esperada = []
        Lista_sharpe_ratio = []
        
        melhor_sharpe_ratio = 1 - sys.maxsize
        melhores_pesos = np.empty
        melhor_volatilidade = 0
        melhor_retorno = 0
        
        for i in range(self.repeticoes):
#            print(i + 1,' ')
    
            pesos = np.random.random(len(self.dataset.columns) - 1)
            pesos = pesos / pesos.sum()
            
            for i in colunas[1:]:
                self.dataset[i] = self.dataset[i] / self.dataset[i][0]
                
            for i, acao in enumerate(self.dataset.columns[1:]):
                self.dataset[acao] = self.dataset[acao] * pesos[i] * self.dinheiro_total
                
            self.dataset.drop(labels = ['Date'], axis = 1, inplace = True)
            
            retorno_carteira = np.log(self.dataset / self.dataset.shift(1))
            matriz_covariancia = retorno_carteira.cov()
            self.dataset['Soma valor'] = self.dataset.sum(axis = 1)
            self.dataset['Taxa de retorno'] = 0.0
            
            for i in range(1, len(self.dataset)):
                self.dataset['Taxa de retorno'][i] = np.log(self.dataset['Soma valor'][i] / self.dataset['Soma valor'][i - 1])
                
            sharpe_ratio = (self.dataset['Taxa retorno'].mean() - self.sem_risco) / (self.dataset['Taxa retorno'].std() * np.sqrt(246))
            retorno_esperado = np.sum(self.dataset['Taxa de retorno'].mean() * pesos) * 246
            volatilidade_esperada = np.sqrt(np.dot(pesos, np.dot(matriz_covariancia * 246, pesos)))
            sharpe_ratio = (retorno_esperado - self.sem_risco) / volatilidade_esperada
            
            if sharpe_ratio > melhor_sharpe_ratio:
                melhor_sharpe_ratio = sharpe_ratio
                melhores_pesos = pesos
                melhor_volatilidade = volatilidade_esperada
                melhor_retorno = retorno_esperado
                
            Lista_retorno_esperado.append(retorno_esperado)
            Lista_volatividade_esperada.append(volatilidade_esperada)
            Lista_sharpe_ratio.append(sharpe_ratio)
            
            self.dataset = dataset_original.copy()
        print()
        a = Alocacao_Ativos(pd.read_csv('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv'), self.dinheiro_total, melhores_pesos = melhores_pesos)
        acoes_pesos, soma_valor,_,_,_,_ = a.alocacao_ativos()

        print(acoes_pesos,'\n')
        print('soma_valor',soma_valor)
        print('Lista_sharpe_ratio ',Lista_sharpe_ratio)

        g = Portifolio(Lista_volatividade_esperada,Lista_retorno_esperado, melhor_volatilidade, melhor_retorno, c = Lista_sharpe_ratio)
        g.portifolio()
        
        print(melhor_sharpe_ratio)
        fim = time.time()
        print('\nTempo de execução Sharpe Ratio: ',(fim - ini) / 60)

        return melhor_sharpe_ratio, melhores_pesos, Lista_retorno_esperado, Lista_volatividade_esperada, Lista_sharpe_ratio, melhor_volatilidade, melhor_retorno
