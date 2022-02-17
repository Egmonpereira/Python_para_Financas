import sys
import random
import numpy as np 

class Sharpe_ratio():
    def __init__(self,dataset, dinheiro_total, sem_risco, repeticoes):
        self.dataset = dataset
        self.dinheiro_total = dinheiro_total
        self.sem_risco = sem_risco
        self.repeticoes = repeticoes
    
        
    def alocacao_portifolio(self):
        self.dataset = self.dataset.copy()
        dataset_original = self.dataset.copy()
        colunas = self.dataset.columns[1:]
        
        melhor_sharpe_ratio = 1 - sys.maxsize
        melhores_pesos = np.empty
        
        for _ in range(self.repeticoes):
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
            self.dataset['Taxa retorno'] = 0.0
            
            for i in range(1, len(self.dataset)):
                self.dataset['Taxa retorno'][i] = np.log(self.dataset['Soma valor'][i] / self.dataset['Soma valor'][i - 1])
                
            #sharpe_ratio = (self.dataset['Taxa retorno'].mean() - self.sem_risco) / (self.dataset['Taxa retorno'].std() * np.sqrt(246))
            retorno_esperado = np.sum(self.dataset['Taxa retorno'].mean() * pesos) * 246
            volatilidade_esperada = np.sqrt(np.dot(pesos, np.dot(matriz_covariancia * 246, pesos)))
            sharpe_ratio = (retorno_esperado - self.sem_risco) / volatilidade_esperada
            
            if sharpe_ratio > melhor_sharpe_ratio:
                melhor_sharpe_ratio = sharpe_ratio
                melhores_pesos = pesos
            
            self.dataset = dataset_original.copy()
            
        return melhor_sharpe_ratio, melhores_pesos
