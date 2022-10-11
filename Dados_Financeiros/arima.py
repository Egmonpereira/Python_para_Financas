import pandas, numpy, datetime
import matplotlib.pyplot as plt
import plotly.express as px

from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_absolute_error

class Arima(object):
    def __init__(self, Lista, Lista_Aux, name, Sai):
        self.Lista = Lista
        self.Lista_Aux = Lista_Aux
        self.name = name
        self.Sai = Sai
    
    def arima(self):
        print('\n:::ARIMA:::\n')
        try:
            dateparse = lambda dates: datetime.datetime.strptime(dates, '%Y-%m-%d')
            dataset = pandas.read_csv('acoesGerais.csv', parse_dates=['Date'], index_col='Date', date_parser = dateparse, usecols=['Date', self.name])
            print(dataset)
        except Exception as erro:
            print(erro)

        time_series = dataset[self.name]
        i = 'n'
        if i != 'n':
            print(time_series['2015-01-08'])
            print(time_series['2015-01-01':'2015-01-10'])
            print(time_series[:'2015-07-31'])
            print(time_series['2015'])
            print(time_series.index.min())
            print(time_series.index.max())
            plt.plot(time_series)
            plt.show()
        
        figura = px.line(title = 'Histórico do preço dos preços das Ações da ' + self.name)
        figura.add_scatter(x = time_series.index, y = time_series)
        figura.show()
        
        time_series_datas = time_series['2015-01-01':'2015-12-31']
        print(time_series_datas)
        plt.plot(time_series_datas)
        plt.show()
                
        decomposicao = seasonal_decompose(time_series, period=len(time_series)//2)
        tendencia = decomposicao.trend
        sazonal = decomposicao.seasonal
        aleatorio = decomposicao.resid
        plt.plot(tendencia)
        plt.show()
        plt.plot(sazonal)
        plt.show()
        
        modelo = auto_arima(time_series, suppress_warnings=True, error_action='ignore')
        #Parametros P, Q e D
        print(modelo.order)
        
        previsoes = modelo.predict(n_periods=90)
        print(previsoes)
        
        treinamento = time_series[:1081]
        teste = time_series[1081:]
        
        modelo2 = auto_arima(treinamento, suppress_warnings=True, error_action='ignore')
        print(modelo2)
        
        previsoes = pandas.DataFrame(modelo2.predict(n_periods=len(teste)), index=teste.index)
        previsoes.columns = ['Previsoes']
        print(previsoes)
        print(teste)
        
        plt.plot(treinamento, label = 'Treinamento')
        plt.plot(teste, label = 'Teste')
        plt.plot(previsoes, label = 'Previsoes')
        plt.legend()
        plt.show()

        print('Calculando o erro')
        print(abs(teste - previsoes['Previsoes']))
        print(abs(teste - previsoes['Previsoes'])/len(teste))
        print(sum(abs(teste - previsoes['Previsoes'])/len(teste)))
        
        print(mean_absolute_error(teste, previsoes))

