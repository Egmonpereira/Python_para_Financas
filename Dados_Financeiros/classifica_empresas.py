#www.bastter.com
#www.tororadar.com
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import pickle

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score, KFold #para trabalhar com informações cruzadas
from sklearn.ensemble import RandomForestClassifier #faz a combinação de várias árvores de decisão
from sklearn.neural_network import MLPClassifier #classe para trabalhar com redes neurais
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV #divide a base de dados

class Classifica_Empresas(object):
    def __init__(self):
        pass

    def classifica_empresas(self):
        print('\n\nCARRGAMENTO E PRÉ-PROCESSAMENTO DA BASE DE DADOS\n')
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

        print('\n\nVISUALIZAÇÃO E EXPLORAÇÃO\n')
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

        dataset.drop(['Rec. Liquida', 'Caixa'], axis = 1, inplace=True)
                
        plt.figure(figsize=(30,50))
        sns.heatmap(dataset.corr(), annot=True, cbar=False)
        #plt.show()

        dataset.drop(['Divida bruta', 'LPA', 'Caixa.1'], axis = 1, inplace=True)
                
        plt.figure(figsize=(30,50))
        sns.heatmap(dataset.corr(), annot=True, cbar=False)
        #plt.show()

        print('\n\nVARIÁVEIS DUMMY\n')
        dataset.drop(['At. Circulante','Liq. Corrente'], axis = 1, inplace=True)
                
        plt.figure(figsize=(30,50))
        sns.heatmap(dataset.corr(), annot=True, cbar=False)
        #plt.show()
                        
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
        print('\n\nX_cat\n\n',X_cat)
        dataset_original = dataset.copy()

        dataset.drop(['Segmento', 'Categoria', 'Situação', 'Empresa'], axis = 1, inplace=True)             
        X_cat.drop([90], axis = 1, inplace = True)
        print(dataset)

        print('\ndataset.index',dataset.index)
        print('\nX_cat.index',X_cat.index)
        dataset.index = X_cat.index
        print(dataset.index, X_cat.index)

        dataset = pd.concat([dataset, X_cat], axis = 1)
        print('\n\nDataset\n\n',dataset)

        print('\n\nNORMALIZAÇÃO\n')
        scaler = MinMaxScaler()
        dataset_normalizado = scaler.fit_transform(dataset)
        print(dataset_normalizado)

        X = dataset_normalizado.copy()
        
        print('\n\nAPLICAÇÃO E AVALIAÇÃO DOS ALGORÍTIMOS\n')
        def forest_neural():
            resultados_forest = []
            resultados_neural = []
            inicio = time.time()
            for i in range(30):
                kfold = KFold(n_splits=10, shuffle=True, random_state=i)

                random_forest = RandomForestClassifier()
                scores = cross_val_score(random_forest, X, y, cv = kfold)
                resultados_forest.append(scores.mean())

                networkd = MLPClassifier(hidden_layer_sizes=(175, 175))
                scores = cross_val_score(networkd, X, y, cv = kfold)
                resultados_neural.append(scores.mean())
            fim = time.time()
            print('\nTempo de Execução: %0.2f' %((fim - inicio)/60))

            resultados_forest = np.array(resultados_forest)
            resultados_neural = np.array(resultados_neural)
            print('resultados_forest\n',resultados_forest)
            print(resultados_forest.mean())
            print('resultados_neural\n',resultados_neural)
            print(resultados_neural.mean())

            print('\n\nAVALIAÇÃO COM BASE DE TREINAMENTO E TESTE\n')
            X_treinamento, X_teste, Y_treinamento, Y_teste = train_test_split(X, y, test_size=0.2) #0.2 pois será usado 20% da base para teste e 80% para treinamento com random forest
            
            print(X_treinamento.shape, Y_treinamento.shape)
            print(X_teste.shape, Y_teste.shape)

            random_forest = RandomForestClassifier()
            print(random_forest)
            print(random_forest.fit(X_treinamento, Y_treinamento))
            
            previsoes = random_forest.predict(X_teste)
            print(previsoes)
            print(Y_teste)
            print(accuracy_score(Y_teste, previsoes))

            cm = confusion_matrix(Y_teste, previsoes)
            print(cm)

            sns.heatmap(cm, annot=True)
            print(random_forest.classes_)
            #plt.show()

            print(classification_report(Y_teste, previsoes))

            print(X_teste[0].shape)
            print(X_teste[0])
            print(X_teste[0].reshape(1,-1))
            print(random_forest.predict(X_teste[0].reshape(1,-1)))
            print(random_forest.feature_importances_)
            print(np.argmax(random_forest.feature_importances_))

            for nome, importancias in zip(dataset.columns, random_forest.feature_importances_):
                print(nome, '=', importancias)

            caracteristicas = dataset
            print(caracteristicas)

            importancias = random_forest.feature_importances_
            print(importancias)
            indices = np.argsort(importancias)
            print(indices)

            try:
                plt.figure(figsize=(40,50))
                plt.title('Importancia das Caracteristicas')
                plt.barh(range(len(indices)), importancias[indices], color = 'b', align = 'center')
                plt.yticks(range(len(indices)), [caracteristicas[i] for i in indices])
                plt.xlabel('Importancias')
                plt.show()
            except:
                print('Gráfico não gerado :-(')

        forest_neural()

        with open('/home/egmon/Yandex/Programacao/Udemy/Python/Python_para_Financas/Bases_de_Dados/bases_classificacao.pkl', 'wb') as f:
            pickle.dump([dataset, dataset_original, X, y, empresa, scaler], f)

        print('EXERCICIO')
        parametros = {'criterion': ['gini','entropy'],
                    'min_samples_split': [2, 4, 6],
                    'n_estimators': [50, 100, 150]}

        grid_search = GridSearchCV(estimator = RandomForestClassifier(), param_grid = parametros)
        grid_search.fit(X,y)
        best_params = grid_search.best_params_
        best_score = grid_search.best_score_
        print(best_params, best_score)