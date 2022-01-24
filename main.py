#br.financas.yahoo.com

import os 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
from pandas_datareader import data 


if __name__ == '__main__':
    os.system('clear')
    
    gol_df = data.DataReader(name = 'GOLL4.SA', data_source = 'yahoo', start = '2015-01-01', end = '2022-01-23')
    print(gol_df)
    print(gol_df.info())
    print(gol_df.head(6))
    print(gol_df.tail())
    print(gol_df.describe())
    print(gol_df[gol_df['Close'] >= 43.79])
    print(gol_df[gol_df['Close'] == 1.16])
    print(gol_df[(gol_df['Close'] >= 1.15) &  (gol_df['Close'] <= 1.16)])
    gol_df.to_csv('Gol.csv')
    gol_df2 = pd.read_csv('Gol.csv')
    print(gol_df2)