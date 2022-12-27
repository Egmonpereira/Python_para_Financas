from asyncore import write
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pickle
import numpy as np
import pandas as pd
import seaborn as sns

class Agrupamento_Empresas(object):
    def __init__(self):
        pass

    def agrupamento_empresas(self):
        print('\n\nPREPARAÇÃO DA BASE DE DADOS\n')
        with open('/home/egmon/Yandex/Programação/Udemy/Python/Python_para_Financas/Bases_de_Dados/bases_classificacao.pkl', 'rb') as f:
            dataset, dataset_original, X, y, empresa, scaler = pickle.load(f)
        print(dataset)
        print(dataset_original)
        print(X)
        print(y)
        print(empresa)
        print(scaler)

        print('\n\nOBTENÇÃO DO NÚMERO DE CLUSTERS')
        wcss = [] #within cluster sum of squares
        faixa = range(1,21)
        for i in faixa:
            kmeans = KMeans(n_clusters=i)
            kmeans.fit(X)
            wcss.append(kmeans.inertia_)
        
        print(wcss)
        try:
            plt.plot(wcss, 'bx-')
            plt.xlabel('Clusters')
            plt.ylabel('WCSS')
            #plt.show()
            print('\nGráfico OK\n')
        except:
            print('\nGráfico com erro\n')

        c = 6#int(input('Quantidade de clusters: '))
        kmeans = KMeans(n_clusters=c)
        kmeans.fit(X)
        print(kmeans)
        labels = kmeans.labels_
        print(len(labels),labels)

        print(np.unique(labels, return_counts=True))

        centroides = pd.DataFrame(data = kmeans.cluster_centers_, columns = [dataset.columns])
        print(centroides)

        print(scaler)
        centroides = scaler.inverse_transform(centroides)
        centroides = pd.DataFrame(data = centroides, columns=[dataset.columns])
        print(centroides)

        dataset_cluster = pd.concat([empresa, pd.DataFrame({'cluster': labels})], axis = 1)
        print(dataset_cluster)

        dataset_cluster = pd.concat([dataset_original, pd.DataFrame({'cluster': labels})], axis = 1)
        print(dataset_cluster)

        categoria_cluster = dataset_cluster.groupby(['Categoria', 'cluster'])['cluster'].count()
        print(categoria_cluster)

        situacao_cluster = dataset_cluster.groupby(['Situação', 'cluster'])['cluster'].count()
        print(situacao_cluster)

        #pd.set_option('max_rows', None)
        segmento_cluster = dataset_cluster.groupby(['Segmento', 'cluster'])['cluster'].count()
        print(segmento_cluster)

        print('\n\nVISUALIZAÇÃO\n')
        pca = PCA(n_components=2)
        componentes = pca.fit_transform(X)
        print(componentes)

        pca_df = pd.DataFrame(data = componentes, columns=['pca1','pca2'])
        pca_df = pd.concat([pca_df, pd.DataFrame({'cluster': labels})], axis = 1)

        try:
            plt.figure(figsize=(10,10))
            sns.scatterplot(x = 'pca1', y = 'pca2', hue = 'cluster', data = pca_df, palette = ['red','green','blue','yellow','black','purple','cyan'])
            #plt.show()
            print('Gráfico OK')
        except:
            print('Gráfico com erro')

        try:
            plt.figure(figsize=(10,10))
            sns.countplot(x = dataset['Situação'])
            #plt.show()
            print('Gráfico OK')
        except:
            print('Gráfico com erro')