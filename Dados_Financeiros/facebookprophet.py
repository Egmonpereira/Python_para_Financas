from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import pandas

class Fbprophet(object):
    def __init__(self, Lista, Lista_Aux, name, Sai):
        self.Lista = Lista
        self.Lista_Aux = Lista_Aux
        self.name = name
        self.Sai = Sai

    def facebookprophet(self):
        print('\n:::FACEBOOK PROPHET EM AÇÃO::\n')
        dataset = pandas.read_csv('/home/egmon/Yandex/Programacao/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv', usecols=['Date', self.name])
        print(dataset)
        dataset = dataset[['Date', self.name]].rename(columns = {'Date': 'ds', self.name: 'y'})
        print(dataset)
        
        modelo = Prophet()
        modelo.fit(dataset)
        
        futuro = modelo.make_future_dataframe(periods=90)
        previsoes = modelo.predict(futuro)
        print(previsoes.head())
        print(len(dataset), len(previsoes))
        print(len(previsoes)-len(dataset))
        print(previsoes.tail(90))

        #Gráficos
        modelo.plot(previsoes, xlabel = 'Data', ylabel = 'Preço').show()
        
        modelo.plot_components(previsoes).show()

        #plot_plotly(modelo, previsoes).show()

        #plot_components_plotly(modelo, previsoes).show()

        pred = modelo.make_future_dataframe(periods=0)
        print(pred)

        previsoes1 = modelo.predict(pred)
        print(previsoes1)

        previsoes1 = previsoes1['yhat'].tail(365)
        print(previsoes1)

        #mean_absolute_error(futuro,previsoes1)
        