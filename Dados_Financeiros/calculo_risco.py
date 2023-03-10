
from unicodedata import name
import pandas as pd 
import numpy as np 
import math 
import matplotlib.pyplot as plt
from pyrsistent import v
from scipy import stats
from graficos import Graficos

class Calculo_Risco():
    def __init__(self,name,Sai):
        self.name = name
        self.Sai = Sai
    
    def calculo_risco(self):
        print('\n:::CÁLCULO DE RISCO:::\n')
        print('self.name,self.Sai',self.name,self.Sai)
        Retorno = []
        print('Taxa de retorno no ano')
        dataset = pd.read_csv('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv')
        
        print('2015:\n',dataset[self.name][dataset['Date'] == '2015-01-02'], '\n',dataset[self.name][dataset['Date'] == '2015-12-30'])
        Retorno.append(np.log(13.5 / 15.2) * 100)
        
        print('\n2016:\n',dataset[self.name][dataset['Date'] == '2016-01-04'], '\n',dataset[self.name][dataset['Date'] == '2016-12-29'])
        Retorno.append(np.log(23.7 / 12.53) * 100)
    
        print('\n2017:\n',dataset[self.name][dataset['Date'] == '2017-01-02'], '\n',dataset[self.name][dataset['Date'] == '2017-12-29'])
        Retorno.append(np.log(48.05 / 23.02) * 100)
        
        print('\n2018:\n',dataset[self.name][dataset['Date'] == '2018-01-02'], '\n',dataset[self.name][dataset['Date'] == '2018-12-28'])
        Retorno.append(np.log(61.18 / 49.88) * 100)
        
        print('\n2019:\n',dataset[self.name][dataset['Date'] == '2019-01-02'], '\n',dataset[self.name][dataset['Date'] == '2019-12-30'])
        Retorno.append(np.log(43.79 / 61.09) * 100)
        
        print('\n2020:\n',dataset[self.name][dataset['Date'] == '2020-01-02'], '\n',dataset[self.name][dataset['Date'] == '2020-10-30'])
        Retorno.append(np.log(12.28 / 44.70) * 100)
        
        Retorno = np.array(Retorno)
        #Retorno.pop()
        #Retorno.append(-128.06)
        print('Retorno',Retorno)
        
        print('\nCálculo da Média: ')
        media_ = Retorno.mean()
        print('Média:\t',media_)
        
        print('\nCálculo da Variância:')
        variancia = Retorno.var()
        print("Variância:\t", variancia)
        
        print(dataset[self.name].tail(330).var())
        
        print('\nCálculo do Desvio Padrão:')
        desvio_Padrao = Retorno.std()
        print('Desvio Padrão:\t',desvio_Padrao)
        
        print('\nCoeficiente de Variação')
        coeficiente_variacao = stats.variation(Retorno) * 100
        print(coeficiente_variacao)
        
        dataset.drop('Date', axis=1, inplace=True)
        
        taxas_Retorno_Simples = (dataset / dataset.shift(1)) - 1
        print(taxas_Retorno_Simples)
        print(taxas_Retorno_Simples.std() * 100)
        
        print('\nAnualizar')
        print(taxas_Retorno_Simples.std() * math.sqrt(246) * 100)
        
        print('Covariância entre Açoes')
        print(taxas_Retorno_Simples.cov())
        
        print('Correlação entre Açoes')
        print(taxas_Retorno_Simples.corr())
        
        g = Graficos('calculo risco', taxas_Retorno_Simples)
        g.graficos()
                
        print('\nRisco de um Portifólio')
        try:
            taxas_Retorno_Simples_Gol_CVC = taxas_Retorno_Simples.drop(columns=self.Sai)
            print(taxas_Retorno_Simples_Gol_CVC)
            print(taxas_Retorno_Simples_Gol_CVC.cov())
            print(taxas_Retorno_Simples_Gol_CVC.cov() * 246)
            pesos = np.array([0.5,0.5])
            aux = np.dot(taxas_Retorno_Simples_Gol_CVC.cov() * 246, pesos)
            variancia = np.dot(aux, pesos)
            print(variancia)
            desvio_Padrao = math.sqrt(variancia)
            print(desvio_Padrao)
        except Exception as erro:
            print(erro)
            
        print('\nRisco de um Portifólio para toda a Carteira')
        Pesos_Carteira1 = np.array([0.2,0.2,0.2,0.2,0.2,0.0])
        print(taxas_Retorno_Simples.cov() * 246)
        aux = np.dot(taxas_Retorno_Simples.cov() * 246, Pesos_Carteira1)
        print('\nVariância do Portifólio 01\n',aux)
        variancia_port1 = np.dot(Pesos_Carteira1,aux)
        print(variancia_port1)
        volatilidade_Portifolio1 = math.sqrt(variancia_port1)
        print(volatilidade_Portifolio1 * 100)
        
        Pesos_Carteira2 = np.array([0.0,0.0,0.0,0.0,0.0,1.0])
        aux = np.dot(taxas_Retorno_Simples.cov() * 246, Pesos_Carteira2)
        
        print('\nVariância do Portifólio 02\n',aux)
        variancia_port2 = np.dot(Pesos_Carteira2,aux)
        print(variancia_port2)
        volatilidade_Portifolio2 = math.sqrt(variancia_port2)
        print()
        print(volatilidade_Portifolio2 * 100)

        variancia_port3 = taxas_Retorno_Simples.var() * 246 * Pesos_Carteira1
        print(variancia_port3)
        
        print('\nRisco não Sistemático 01')
        sub1 = 0
        for i in range(1,len(variancia_port3)):
            sub1 += variancia_port3[i]
            
        sub1 = variancia_port3[0] - sub1
        print(sub1)
        risco_nao_sistematico1 = variancia_port2 - sub1
        print(risco_nao_sistematico1)
            
        print('\nRisco não Sistemático 02')
        sub2 = 0
        for i in range(1,len(variancia_port3)):
            sub2 += variancia_port3[i]
            
        sub2 = variancia_port3[0] - sub2
        print(sub2)
        risco_nao_sistematico2 = variancia_port2 - sub2
        print(risco_nao_sistematico2)
        
        return Retorno