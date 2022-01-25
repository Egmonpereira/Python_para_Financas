import pandas as pd 
import numpy as np 
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns 

class Graficos(object):
    def __init__(self):
        pass
    def graficos():
                
        acoes_df = pd.read_csv('acoesGeral.csv')
        
        #plt.figure(figsize=(50,10))
        '''
        i = 1
        for i in np.arange(1, len(acoes_df.columns)):
            plt.subplot(7,1,i + 1)
            sns.histplot(acoes_df[acoes_df.columns[i]], kde = True)
            plt.title(acoes_df.columns[i])
            plt.show()
        
        i = 1
        for i in np.arange(1, len(acoes_df.columns)):
            plt.subplot(7,1,i + 1)
            sns.boxplot(x = acoes_df[acoes_df.columns[i]])
            plt.title(acoes_df.columns[i])
            plt.show()
        '''
