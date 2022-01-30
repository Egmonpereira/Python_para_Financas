import os 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import plotly.express as px 
import random

def alocacao_ativos(dataset, grana, seed = 0):
    dataset = dataset.copy()
    
    if seed != 0:
        np.random.seed(seed)
    pesos = np.random.random(len(dataset.columns)-1)
    pesos = pesos / pesos.sum()
    print(pesos,pesos.sum())
    
    colunas = dataset.columns[1:]
    for i in colunas:
        dataset[i] = dataset[i] / dataset[i][0]
        
    for i, acao in enumerate(dataset.columns[1:]):
        dataset[acao] = dataset[acao] * pesos[i] * grana
    
    dataset['Soma valor'] = dataset.sum(axis = 1)
    
    datas = dataset['Date']
    dataset.drop(labels = ['Date'], axis = 1, inplace = True)
    
    dataset['Taxa de Retorno'] = 0.0
    
    for i in range(1,len(dataset)):
        dataset['Taxa de Retorno'][i] = ((dataset['Soma valor'][i]) / (dataset['Soma valor'][i - 1]) -1 ) * 100
    
    acoes_pesos = pd.DataFrame(data = {'Acões': colunas, 'Pesos': pesos * 100})
    
    print(dataset, datas, acoes_pesos, '\n',dataset.loc[len(dataset) - 1]['Soma valor'])
    
    figura = px.line(x = datas, y = dataset['Taxa de Retorno'], title = 'Retorno diário do Portifólio')
    figura.show()
    
    figura = px.line(title='Evolução do Patrimônio')
    for i in dataset.columns:
        figura.add_scatter(x = datas, y = dataset[i], name = i)
    figura.show()
    
    figura = px.line(x = datas, y = dataset['Soma valor'], title = 'Retorno diário do Portifólio')
    figura.show()
    
    
if __name__ == '__main__':
    os.system('clear')
    
    Lista = ['GOLL4.SA','CVCB3.SA','WEGE3.SA','MGLU3.SA','TOTS3.SA','BOVA11.SA']
    Lista_Aux = ['GOL','CVC','WEGE','MAGALU','TOTS','BOVA']

#    Lista = ['TIMB','VIVT3.SA','PETR3.SA','BBAS3.SA','CMIG4.SA','VALE3.SA']
#    Lista_Aux = ['TIM','VIVO','PETROBRAS','BBRASIL','CEMIG','VALE']

#    Lista = ['ABEV3.SA','ODPV3.SA','VIVT3.SA','PETR3.SA','BBAS3.SA','BOVA11.SA']
#    Lista_Aux = ['AMBEV','ODONTOPREV','VIVO','PETROBRAS','BBRASIL','BOVA']

    dataset = pd.read_csv('acoesGeral.csv')
    
    alocacao_ativos(dataset,5000,10)