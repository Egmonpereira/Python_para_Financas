#import mlrose
import numpy

class Otimizacao_Portifolio(object):
    def __init__(self,dataset, dinheiro_total, sem_risco):
        self.dataset = dataset 
        self.dinheiro_total = dinheiro_total
        self.sem_risco = sem_risco
    
    def otimizacao_portifolio(self):
        numpy.random.seed(10)
        pesos = numpy.random.random(len(self.dataset.columns) - 1)
        pesos = pesos / pesos.sum()
        
        #Função de custo
        def fitness_function(solucao):
            dataset = self.dataset.copy()
            pesos = solucao / solucao.sum()
        
            for i in dataset.columns[1:]:
                dataset[i] = (dataset[i] / dataset[i][0])
                
            for i, acao in enumerate(dataset.columns[1:]):
                dataset[acao] = dataset[acao] * pesos[i] * self.dinheiro_total
                
            dataset.drop(labels = ['Date'], axis = 1, inplace = True)
            dataset['Soma Valores'] = dataset.sum(axis = 1)
            dataset['Taxa de Retorno'] = 0.0
            
            for i in range(1, len(dataset)):
                dataset['Taxa de Retorno'][i] = ((dataset['Soma Valores'][i] / dataset['Soma Valores'][i - 1]) - 1) * 100
                
            sharpe_ratio = (dataset['Taxa de Retorno'].mean() - self.sem_risco) / dataset["Taxa de Retorno"].std() * numpy.sqrt(246)
                
            
            return sharpe_ratio
        
        def visualiza_alocacao(solucao):
            colunas = self.dataset.columns[1:]
            
            for i in range(len(solucao)):
                print(colunas[i], solucao[i] * 100)
        
        print('\nSharpe Ratio',fitness_function(pesos))
        
        visualiza_alocacao(pesos)
