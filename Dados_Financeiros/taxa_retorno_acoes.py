import pandas as pd 
import numpy as np 
import plotly.express as px
import matplotlib.pyplot as plt
from graficos import Graficos

class Taxa_Retorno_Acoes(object):
    def __init__(self,Lista,Lista_Aux):
        self.Lista = Lista
        self.Lista_Aux = Lista_Aux
    
    def taxa_retorno_acoes(self):
        
        dataset = pd.read_csv('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv')
        
        for i in range(1,len(dataset.columns)):
            #Taxa de retorno simples é usada para comparar várias ações no mesmo período
            print(dataset.columns[i],'\t=',((dataset[dataset.columns[i]][len(dataset) - 1] - dataset[dataset.columns[i]][0])/(dataset[dataset.columns[i]][0])) * 100)
            for i in range(len(self.Lista)):
                dataset['RS ' + self.Lista_Aux[i]] = (dataset[self.Lista_Aux[i]] / dataset[self.Lista_Aux[i]].shift(1)) - 1
        
        print()
        print('Taxa de retorno simples diária - Média')
        for i in range(len(self.Lista)):
            print(self.Lista_Aux[i],'\t= ',dataset['RS ' + self.Lista_Aux[i]].mean()) #Taxa de retorno diária

        print()
        print('Taxa de retorno simples anual - Média')
        for i in range(len(self.Lista)):
            print(self.Lista_Aux[i],'\t= ',dataset['RS ' + self.Lista_Aux[i]].mean() * (246) * 100) #Taxa de retorno anual
            
        print()
        for i in range(len(self.Lista_Aux)):
            #Taxa de retorno Logarítmica é usada para comparar uma única ação em vários períodos de tempo
            dataset['RL ' + self.Lista_Aux[i]] = np.log(dataset[self.Lista_Aux[i]] / dataset[self.Lista_Aux[i]].shift(1))

        print('Taxa de retorno Logarítmica diária - Média')
        for i in range(len(self.Lista_Aux)):
            print('RL ' + self.Lista_Aux[i],'\t=' ,dataset['RL ' + self.Lista_Aux[i]].mean())
        
        print()
        print('Taxa de retorno Logarítmica anual - Média')
        for i in range(len(self.Lista)):
            print('RL ' + self.Lista_Aux[i],'\t= ',dataset['RL ' + self.Lista_Aux[i]].mean() * (246) * 100) #Taxa de retorno anual

        dataset = pd.read_csv('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv')
        dataset_normalizado = dataset.copy()
        
        for i in dataset_normalizado.columns[1:]:
            dataset_normalizado[i] = dataset_normalizado[i] / dataset_normalizado[i][0]

        g = Graficos('taxa normalizado', dataset_normalizado)
        g.graficos()        
        
        dataset_normalizado.drop(labels=['Date'], axis = 1, inplace=True)
        retorno_carteira = (dataset_normalizado / dataset_normalizado.shift(1)) - 1
        
        retorno_anual = retorno_carteira.mean() * 246
        print(retorno_anual)
        
        print(retorno_anual * 100)
        
        Pesos_Carteira1 = np.array([0.2,0.2,0.2,0.2,0.2,0.0])
        print('Carteira sem a BOVA',np.dot(retorno_anual * 100,Pesos_Carteira1))    
        
        Pesos_Carteira2 = np.array([0.1,0.2,0.2,0.2,0.1,0.2])
        print('Carteira com a BOVA',np.dot(retorno_anual * 100,Pesos_Carteira2))
        
        dataset = pd.read_csv('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv')
        dataset_normalizado = dataset.copy()
        
        for i in dataset_normalizado.columns[1:]:
            dataset_normalizado[i] = dataset_normalizado[i] / dataset_normalizado[i][0]

        for i in range(len(self.Lista_Aux[0])):
            dataset_normalizado['CARTEIRA'] = dataset_normalizado[self.Lista_Aux[i]]
            
        print(dataset_normalizado.head())
        dataset_normalizado['CARTEIRA'] = dataset_normalizado['CARTEIRA'] / 5
        print(dataset_normalizado.head())

        g = Graficos('comparativo', dataset_normalizado)
        g.graficos()            
        
        for i in range(len(self.Lista_Aux) - 1):
            dataset_normalizado.drop([self.Lista_Aux[i]],axis = 1, inplace=True)
        print(dataset_normalizado)

        g = Graficos('comparativo normalizado', dataset_normalizado)        
        g.graficos()
        
        return dataset