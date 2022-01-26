from cProfile import label
import math
import os 

import pandas as pd 
import numpy as np 
import plotly.express as px
import matplotlib.pyplot as plt




if __name__ == '__main__':
    os.system('clear')

#    Lista = ['GOLL4.SA','CVCB3.SA','WEGE3.SA','MGLU3.SA','TOTS3.SA','BOVA11.SA']
#    Lista_Aux = ['GOL','CVC','WEGE','MAGALU','TOTS','BOVA']
    Lista = ['ABEV3.SA','ODPV3.SA','TIMB','VIVT3.SA','PETR3.SA','BBAS3.SA','CMIG4.SA','VALE3.SA','BOVA11.SA']
    Lista_Aux = ['AMBEV','ODONTOPREV','TIM','VIVO','PETROBRAS','BBRASIL','CEMIG','VALE','BOVA']


    dataset = pd.read_csv('/home/egmon/Yandex/Programação/Python/Udemy/Python/Python_para_Financas/acoesGeral.csv')
    
    for i in range(1,len(dataset.columns)):
        #Taxa de retorno simples é usada para comparar várias ações no mesmo período
        print(dataset.columns[i],'\t=',((dataset[dataset.columns[i]][len(dataset) - 1] - dataset[dataset.columns[i]][0])/(dataset[dataset.columns[i]][0])) * 100)
        for i in range(len(Lista)):
            dataset['RS ' + Lista_Aux[i]] = (dataset[Lista_Aux[i]] / dataset[Lista_Aux[i]].shift(1)) - 1
    
    print()
    print('Taxa de retorno simples diária - Média')
    for i in range(len(Lista)):
        print(Lista_Aux[i],'\t= ',dataset['RS ' + Lista_Aux[i]].mean()) #Taxa de retorno diária

    print()
    print('Taxa de retorno simples anual - Média')
    for i in range(len(Lista)):
        print(Lista_Aux[i],'\t= ',dataset['RS ' + Lista_Aux[i]].mean() * (246) * 100) #Taxa de retorno anual
        
    print()
    for i in range(len(Lista_Aux)):
        #Taxa de retorno Logarítmica é usada para comparar uma única ação em vários períodos de tempo
        dataset['RL ' + Lista_Aux[i]] = np.log(dataset[Lista_Aux[i]] / dataset[Lista_Aux[i]].shift(1))

    print('Taxa de retorno Logarítmica diária - Média')
    for i in range(len(Lista_Aux)):
        print('RL ' + Lista_Aux[i],'\t=' ,dataset['RL ' + Lista_Aux[i]].mean())
    
    print()
    print('Taxa de retorno Logarítmica anual - Média')
    for i in range(len(Lista)):
        print('RL ' + Lista_Aux[i],'\t= ',dataset['RL ' + Lista_Aux[i]].mean() * (246) * 100) #Taxa de retorno anual

    dataset = pd.read_csv('acoesGeral.csv')
    dataset_normalizado = dataset.copy()
    
    for i in dataset_normalizado.columns[1:]:
        dataset_normalizado[i] = dataset_normalizado[i] / dataset_normalizado[i][0]

    
    dataset_normalizado.plot(x = 'Date')
    plt.show()
    
    dataset_normalizado.drop(labels=['Date'], axis = 1, inplace=True)
    retorno_carteira = (dataset_normalizado / dataset_normalizado.shift(1)) - 1
    
    retorno_anual = retorno_carteira.mean() * 246
    print(retorno_anual)
    
    print(retorno_anual * 100)
    
    Pesos_Carteira1 = np.array([0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.0])
    print('Carteira sem a BOVA',np.dot(retorno_anual * 100,Pesos_Carteira1))    
    
    Pesos_Carteira2 = np.array([0.1,0.1,0.2,0.1,0.1,0.1,0.1,0.1,0.1])
    print('Carteira com a BOVA',np.dot(retorno_anual * 100,Pesos_Carteira2))
    
    dataset = pd.read_csv('acoesGeral.csv')
    dataset_normalizado = dataset.copy()
    
    for i in dataset_normalizado.columns[1:]:
        dataset_normalizado[i] = dataset_normalizado[i] / dataset_normalizado[i][0]

    for i in range(len(Lista_Aux[0])):
        dataset_normalizado['CARTEIRA'] = dataset_normalizado[Lista_Aux[i]]
        
    print(dataset_normalizado.head())
    dataset_normalizado['CARTEIRA'] = dataset_normalizado['CARTEIRA'] / 5
    print(dataset_normalizado.head())
    
    figura = px.line(title = 'Comparativo Carteria BOVA')
    for i in dataset_normalizado.columns[1:]:
        figura.add_scatter(x = dataset_normalizado['Date'], y = dataset_normalizado[i], name = i)
        
    figura.show()
    
    for i in range(len(Lista_Aux) - 1):
        dataset_normalizado.drop([Lista_Aux[i]],axis = 1, inplace=True)
    print(dataset_normalizado)
    
    figura = px.line(title = 'Comparativo Carteria BOVA')
    for i in dataset_normalizado.columns[1:]:
        figura.add_scatter(x = dataset_normalizado['Date'], y = dataset_normalizado[i], name = i)
        
    figura.show()
    