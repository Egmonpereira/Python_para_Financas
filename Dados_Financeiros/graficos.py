from mailbox import mbox
from unicodedata import name
import pandas as pd 
import numpy as np 
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns 

class Graficos(object):
    def __init__(self,funcao, acoes_df):
        self.funcao = funcao
        self.acoes_df = acoes_df
        
    def graficos(self):
        s = 'n'#input('Gerar Gráficos S/N: ').lower()
        if s == 's':
            if self.funcao == "acoesgerais":
                self.acoes_df.plot(x = 'Date', title = 'Histórico do preço das ações')
                #plt.show()
                
                i = 1
                for i in np.arange(1, len(self.acoes_df.columns)):
                    plt.figure(figsize=(50,10))
                    plt.subplot(7,1,i + 1)
                    sns.histplot(self.acoes_df[self.acoes_df.columns[i]], kde = True)
                    plt.title(self.acoes_df.columns[i])
                    #plt.show()

                i = 1
                for i in np.arange(1, len(self.acoes_df.columns)):
                    plt.figure(figsize=(50,10))
                    plt.subplot(7,1,i + 1)
                    sns.boxplot(x = self.acoes_df[self.acoes_df.columns[i]])
                    plt.title(self.acoes_df.columns[i])
                    #plt.show()

        
            elif self.funcao == 'normalizado':        
                self.acoes_df.plot(x = 'Date', title = 'Histórico do preço das ações - noramalizados')
                #plt.show()
                
            elif self.funcao == 'historico':
                figura = px.line(title = 'Histórico do preço das ações')
                for i in self.acoes_df.columns[1:]:
                    figura.add_scatter(x = self.acoes_df['Date'], y = self.acoes_df[i], name = i)
            
                figura.show()
                
            elif self.funcao == 'historico normalizado':
                figura2 = px.line(title = 'Histórico do preço das ações - noramalizados')
                for i in self.acoes_df.columns[1:]:
                    figura2.add_scatter(x = self.acoes_df['Date'], y = self.acoes_df[i], name = i)
                    
                figura2.show()
                
            elif self.funcao == 'taxa normalizado':
                self.acoes_df.plot(x = 'Date')
                #plt.show()
                
            elif self.funcao == 'comparativo':
                figura = px.line(title = 'Comparativo Carteria BOVA')
                for i in self.acoes_df.columns[1:]:
                    figura.add_scatter(x = self.acoes_df['Date'], y = self.acoes_df[i], name = i)
                figura.show()
                
            elif self.funcao == 'comparativo normalizado':
                figura = px.line(title = 'Comparativo Carteria BOVA')
                for i in self.acoes_df.columns[1:]:
                    figura.add_scatter(x = self.acoes_df['Date'], y = self.acoes_df[i], name = i)
                figura.show()

            elif self.funcao == 'calculo risco':
                sns.heatmap(self.acoes_df.corr(), annot=True)
                #plt.show()

            elif self.funcao == 'alocacao':
                datas = self.acoes_df['Date']
                self.acoes_df.drop(labels = ['Date'], axis = 1, inplace = True)
                figura = px.line(x = datas, y = self.acoes_df['Taxa de Retorno'], title = 'Retorno diário do Portifólio')
                figura.show()
        
                figura = px.line(title='Evolução do Patrimônio')
                for i in self.acoes_df.columns:
                    figura.add_scatter(x = datas, y = self.acoes_df[i], name = i)
                figura.show()
        
                figura = px.line(x = datas, y = self.acoes_df['Soma valor'], title = 'Retorno diário do Portifólio')
                figura.show()
        
        else:
            print("Nenhum gráfico exigido!")
        
        plt.show()


class Portifolio(object): 
    def __init__(self,Lve,Lre, mv, mr, c = []):
        self.Lve = Lve
        self.Lre = Lre
        self.mv = mv
        self.mr = mr
        self.c = c
    
    def portifolio(self):
        s = 'n'#input('Gerar Gráficos S/N: ').lower()
        if s == 's':
            plt.figure()
            plt.scatter(self.Lve,self.Lre, self.c)
            plt.colorbar(label = 'Sharpe Ratio')
            plt.xlabel('Volatilidade')
            plt.ylabel('Retorno')
            plt.scatter(self.mv, self.mr, c = 'red', s = 100)
            plt.show()

class Grafico_Capm(object):
    def __init__(self,dataset, beta, alpha):
        self.dataset = dataset
        self.beta = beta
        self.alpha = alpha

    def grafico_Capm(self):
        figura = px.scatter(self.dataset, x = 'BOVA', y = 'MAGALU', title = 'BOVA X MAGALU')
        figura.add_scatter(x = self.dataset['BOVA'], y = self.beta * self.dataset['BOVA'] + self.alpha)
        figura.show()

class Grafico_smc(object):
    def __init__(self, dataset, Z, previsoes, dataset_acao, acao):
        self.dataset = dataset
        self.Z = Z
        self.previsoes = previsoes
        self.dataset_acao = dataset_acao
        self.acao = acao

    def grafico_smc(self):
        figura = px.line(title = 'Histórico do preço das Ações')
        for i in self.dataset.columns[1:]:
            figura.add_scatter(x = self.dataset['Date'], y = self.dataset[i], name = i)
        figura.show()

        figura = px.line(title = 'Histórico do preço das Ações da ' + self.acao)
        figura.add_scatter(x = self.dataset['Date'], y = self.dataset[self.acao], name = self.acao)
        figura.show()

        sns.histplot(self.Z)
        plt.show()

    def grafico_previsoes(self):
        figura = px.line(title = 'Previsões do preço das Ações - Monte Carlo - ' + self.acao)
        for i in range(len(self.previsoes)):
            figura.add_scatter(y = self.previsoes[i], name = i)
        figura.show()

    def grafico_simulacao(self):
        figura = px.line(title = 'Simulação do preço das Ações da ' + self.acao)
        figura.add_scatter(y = self.dataset_acao, name = 'Valor real')
        figura.show()