from pandas_datareader import data
import pandas as pd 
import numpy as np 
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

from graficos import Graficos 

class AcoesGerais(object):
    def __init__(self,Lista,Lista_Aux):
        self.Lista = Lista
        self.Lista_Aux = Lista_Aux
    
    def retorna(self):
        return self.Lista, self.Lista_Aux
    
    def acoesGerais(self):
        acoes_df = pd.DataFrame()

        for i in self.Lista:
            acoes_df[i] = data.DataReader(i, data_source = 'yahoo', start = '2015-01-01', end = '2022-11-03')['Close']
        
        for i in range(len(self.Lista)):
            acoes_df = acoes_df.rename(columns={self.Lista[i]: self.Lista_Aux[i]})
        
        acoes_df.dropna(inplace=True)
        print(acoes_df.isnull().sum())
        print(acoes_df)
        acoes_df.to_csv('acoesGerais.csv')
        print(acoes_df.columns[1:])
        print(acoes_df.describe())

        #sns.histplot(acoes_df['GOL'], kde=True)
        #sns.boxplot(x = acoes_df['GOL'])
        
        acoes_df = pd.read_csv('acoesGerais.csv')

#        acoes_df.plot(x = 'Date', title = 'Histórico do preço das ações')
#        plt.show()
        
        acoes_df_normalizado = acoes_df.copy()
        for i in acoes_df_normalizado.columns[1:]:
            acoes_df_normalizado[i] = acoes_df_normalizado[i] / acoes_df_normalizado[i][0]
        print(acoes_df_normalizado)

#        acoes_df_normalizado.plot(x = 'Date', title = 'Histórico do preço das ações - noramalizados')
#        plt.show()
        '''
        figura = px.line(title = 'Histórico do preço das ações')
        for i in acoes_df.columns[1:]:
            figura.add_scatter(x = acoes_df['Date'], y = acoes_df[i], name = i)
        
        figura.show()
        '''
        figura2 = px.line(title = 'Histórico do preço das ações - noramalizados')
        for i in acoes_df_normalizado.columns[1:]:
            figura2.add_scatter(x = acoes_df_normalizado['Date'], y = acoes_df_normalizado[i], name = i)
         
        #Comentado para agilizar não imprimindo gráficos
        #figura2.show()
        
        #Graficos.graficos()
