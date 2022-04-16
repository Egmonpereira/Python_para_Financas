from fbprophet import Prophet
import pandas

class Fbprophet(object):
    def __init__(self, Lista, Lista_Aux, name, Sai):
        self.Lista = Lista
        self.Lista_Aux = Lista_Aux
        self.name = name
        self.Sai = Sai

    def facebookprophet(self):
        dataset = pandas.read_csv('acoesGerais.csv', usecols=['Date', self.name])
        print(dataset)
        dataset = dataset[['Date', self.name]].rename(columns = {'Date': 'ds', self.name: 'y'})
        print(dataset)
        
        modelo = Prophet()
        modelo.fit(dataset)
        
        futuro = modelo.make_future_dataframe(periods=90)
        previsoes = modelo.predict(futuro)