import spacy
import pandas as pd
import string
import matplotlib.pyplot as plt
import seaborn as sns
import random
import numpy as np
import re
import time

from wordcloud import WordCloud
from spacy import displacy

class Analise_Sentimentos(object):
    def __init__(self):
        pass

    def analise_sentimentos(self):

        #Carregamento da base de dados
        base = pd.read_csv('/home/egmon/Yandex/Programacao/Udemy/Python/Python_para_Financas/Bases_de_Dados/stock_data.csv')
        print(base.head())
        print(base.tail())
        print(np.unique(base['Sentiment'], return_counts=True))
        
        #Grafico 01
        sns.countplot(x = base['Sentiment'])
        #plt.show()
        
        print(base.isnull().sum())

        #Função para pré-processamento dos textos
        pln = spacy.load('en_core_web_sm')
        print('\nTrabalhando com linguagem:',pln,'\n')

        stop_words = spacy.lang.en.stop_words.STOP_WORDS
        #print(stop_words)

        def preprocessamento(texto):
            texto = texto.lower()
            texto = re.sub(r'@[A-Za-z0-9$-_@.&+]+', ' ', texto)
            texto = re.sub(r'https?://[A-Za-z0-9./_]+', ' ', texto)
            texto = re.sub(r' +', ' ', texto)

            documento = pln(texto)
            Lista = []
            for token in documento:
                Lista.append(token.lemma_)

            Lista = [palavra for palavra in Lista if palavra not in stop_words and palavra not in string.punctuation]
            Lista = ' '.join([str(elemento) for elemento in Lista if not elemento.isdigit()])

            return Lista

        print(preprocessamento("I will by the Apple stock Hello Word! @test 22 Egmon care caring de mim http://www.egmon.com ok "))
        
        #Limpeza dos textos
        print(base.head(10))
        inicio = time.time()
        base['Text'] = base['Text'].apply(preprocessamento)
        fim = time.time()
        
        print(base.head(10))

        #Número médio de caracteres
        base['Tam'] = base['Text'].apply(len)
        print(base.head())

        print(base['Tam'].describe())

        positivo = base[base['Sentiment'] == 1]
        print('\nPositivo\n',positivo['Tam'].describe())

        negativo = base[base['Sentiment'] == -1]
        print('\nNegativo\n',negativo['Tam'].describe())

        textos_positivos = positivo['Text'].tolist()
        textos_positivos_string = ' '.join(textos_positivos)
        print(textos_positivos_string)

        plt.figure(figsize=(20,10))
        plt.imshow(WordCloud().generate(textos_positivos_string))
        #plt.show()

        textos_negativos = negativo['Text'].tolist()
        textos_negativos_string = ' '.join(textos_negativos)
        print(textos_negativos_string)

        plt.figure(figsize=(20,10))
        plt.imshow(WordCloud().generate(textos_negativos_string))
        #plt.show()

        #Extração de entidades nomeadas
        documento = pln(textos_positivos_string)
        displacy.render(documento, style = 'ent', jupyter = True)

        empresas_positivas = []
        for entidade in documento.ents:
            if entidade.label == 'ORG':
                print(entidade.text, entidade.label_)
                empresas_positivas.append(entidade.text)

        empresas_positivas = set(empresas_positivas)
        print(empresas_positivas)

        print('\nTempo: %0.2f' %((fim - inicio)/60))