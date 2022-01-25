import os 

import pandas as pd 
import numpy as np 
import plotly.express as px
from sklearn import datasets 

if __name__ == '__main__':
    os.system('clear')
    
    dataset = pd.read_csv('/home/egmon/Yandex/Programação/Python/Udemy/Python/Python_para_Financas/acoesGeral.csv')
    
    for i in range(1,len(dataset.columns)):
        print(dataset.columns[i],'\t=',((dataset[dataset.columns[i]][len(dataset) - 1] - dataset[dataset.columns[i]][0])/(dataset[dataset.columns[i]][0])) * 100)