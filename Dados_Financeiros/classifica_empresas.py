#www.bastter.com
#www.tororadar.com
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler

class Classifica_Empresas(object):
    def __init__(self):
        pass

    def classifica_empresas(self):
        dataset = pd.read_excel('/home/egmon/Yandex/Programacao/Udemy/Python/Python_para_Financas/Bases_de_Dados/BD_Completo.xlsx')
        #print(sns.heatmap(dataset.isnull()))
        #plt.show()
        print(dataset.isnull())
        #pd.set_option('max_rows', None)
        print(dataset.isnull().sum())
        dataset.drop(labels = ['EV/EBITDA','DPA','Dividend Yield','Payout','Luc. Liq * NR','Resultado Bruto','Margem Bruta','EBIT','D&A','EBITDA','Margem EBITDA','Res. Financeiro','ROA','SSS','RIF','Margem Bancaria','Indc. Eficiencia','Indc. Basileia','PDD','Patri. Liquido','Despesas com juros','Custo % da divida','IPL','FCO','FCI','FCF','FCT','FCL','FCI/LL','CAPEX','FCL CAPEX','CAPEX/LL','CAPEX/FCO','Majoritar.','PDD/LL','Equity Multi.','Div Liquida/EBITDA','Indice de Cobertura'], axis = 1, inplace = True)
        print(dataset.shape)
        print(dataset.isnull().sum())
        dataset.fillna(dataset.mean(), inplace=True)
        print(dataset.isnull().sum())
        dataset.dropna(inplace=True)
        print(dataset.shape)

        #VISUALIZAÇÃO E EXPLORAÇÃO
        print(dataset.info())
        plt.figure(figsize=(15,15))
        sns.countplot(x = dataset['Situação'])
        #plt.show()
        print(np.unique(dataset['Situação'],return_counts=True))
        print(np.unique(dataset['Segmento'], return_counts=True))
        def corrige_segmento(texto):
            segmento = ""
            if texto == "acessórios":
                segmento = 'acessorios'
            elif texto == "agriculltura":
                segmento = 'agricultura'
            elif texto == 'alimentos diversos':
                segmento = 'alimentos'
            elif texto == 'eletrodomésticos':
                segmento = 'eletrodomesticos'
            elif texto == 'equipamentos e servicos':
                segmento = 'equipamentos'
            elif texto == 'mateial rodoviario':
                segmento = 'material rodoviario'
            elif texto == 'ser med hospt analises e diagnosticos0' or texto == 'serv med hospt analises e diagnosticos' or texto == 'serv. Med. Hospit. Analises e diagnosticos' or texto == 'serv.med.hospit.analises e diagnosticos':
                segmento = 'hospitalar'
            elif texto == 'serviços de apoio e armazenamento':
                segmento = 'serviços de apoio e armazenagem'
            elif texto == 'serviços diversos s.a ctax':
                segmento = 'serviços diversos'
            elif texto == 'siderurgia':
                segmento = 'siderurgica'
            elif texto == 'soc credito e financiamento' or texto == 'soc. Credito e financiamento':
                segmento = 'credito'
            elif texto == 'tansporte aereo':
                segmento = 'transporte aereo'
            else:
                segmento = texto
        
            return segmento
        
        dataset['Segmento'] = dataset['Segmento'].apply(corrige_segmento)
        #print(np.unique(dataset['Segmento'], return_counts=True))
        print(np.unique(dataset['Categoria'], return_counts=True))

        def corrige_categoria(texto):
            categoria = ''
            if texto == 'crescimento ':
                categoria = 'crescimento'
            else:
                categoria = texto
            return categoria

        dataset['Categoria'] = dataset['Categoria'].apply(corrige_categoria)
        print(np.unique(dataset['Categoria'], return_counts=True))

        plt.figure(figsize=(15,15))
        sns.countplot(x = dataset['Categoria'])
        #plt.show()

        print(dataset.describe())

        print(dataset[dataset['LPA']== -806.670000])

        print(dataset[dataset['LPA']== 200.660000])

        print(dataset[dataset['LPA desconctado']== -806.660000])

        print(dataset[dataset['LPA desconctado']== 160.780000])

        print(dataset[dataset['Caixa']== -0.125000])
        
        print(dataset[dataset['Caixa']== 59223.000000])

        print(dataset[dataset['Divida Liquida']== 199245.000000])
        
        figura = plt.figure(figsize=(30,50))
        eixo = figura.gca()
        dataset.hist(ax = eixo)
        #plt.show()

        plt.figure(figsize=(30,50))
        sns.heatmap(dataset.corr(), annot=True, cbar=False)
        #plt.show()

        dataset.drop(['Rec. Liquida', "Caixa", 'Divida bruta', 'LPA', 'Caixa.1','At. Circulante','Liq. Corrente'], axis = 1, inplace=True)
                
        plt.figure(figsize=(30,50))
        sns.heatmap(dataset.corr(), annot=True, cbar=False)
        #plt.show()

        #Variáveis Dummy
        y = dataset['Situação'].values
        empresa = dataset['Empresa']
        X_cat = dataset[['Segmento','Categoria']]
        print(y)
        print(empresa)
        print(X_cat)

        onehotencoder = OneHotEncoder()
        X_cat = onehotencoder.fit_transform(X_cat).toarray()
        print(X_cat)
        X_cat = pd.DataFrame(X_cat)
        print(X_cat)
        dataset_original = dataset.copy()

        dataset.drop(['Situação', 'Segmento', 'Categoria', 'Empresa'], axis = 1, inplace=True)             
        print(dataset)

        dataset.index = X_cat.index
        print(dataset.index, X_cat.index)

        dataset = pd.concat([dataset, X_cat], axis = 1)
        print(dataset)

        #NORMALIZAÇÃO
        scaler = MinMaxScaler()
        dataset_normalizado = scaler.fit_transform(dataset)
        print(dataset_normalizado)

        X = dataset_normalizado.copy()
        