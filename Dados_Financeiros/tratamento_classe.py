from clean import Clean
from analise_sentimentos import Analise_Sentimentos

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import pandas, spacy, random, numpy, re 
import matplotlib.pyplot as plt
import seaborn as sns

class Tratamento_classe(object):
    def self(self):
        pass

    def tratamento_classe(self):
        base = pandas.read_csv('/home/egmon/Yandex/Programação/Udemy/Python/Python_para_Financas/Bases_de_Dados/stock_data.csv')
        print(base.head())
        
        base_treinamento, base_teste = train_test_split(base, test_size=0.3)
        print('base_treinamento:', base_treinamento.shape)
        print('base_teste:', base_teste.shape)

        exemplo_base_dados = [['Este trabalho eh agradavel', {'POSITIVO': True, 'NEGATIVO': False}],
                                ['Este lugar continua assustador', {'POSITIVO': False, 'NEGATIVO': True}]]

        base_treinamento_final = []
        for texto, sentimento in zip(base_treinamento['Text'], base_treinamento['Sentiment']):
            if sentimento == 1:
                dic = ({'POSITIVO': True, 'NEGATIVO': False})
            elif sentimento == -1:
                dic = ({'POSITIVO': False, 'NEGATIVO': True})
            base_treinamento_final.append([texto, dic.copy()])

        print(base_treinamento_final[10:15])
        print(len(base_treinamento_final))


        #Criação do Classificador
        modelo = spacy.blank('en')
        categorias = modelo.create_pipe('textcat')
        categorias.add_label('POSITIVO')
        categorias.add_label('NEGATIVO')
        modelo.add_pipe(categorias)
        historico = []

        modelo.begin_training()
        for epoca in range(5):
            random.shuffle(base_treinamento_final)
            erros = {}
            for batch in spacy.util.minibatch(base_treinamento_final, 512):
                textos = [modelo(texto) for texto, entities in batch]
                annotations = [{'cats': entities} for texto, entities in batch]
                modelo.update(textos, annotations, losses = erros)
                historico.append(erros)
            if epoca % 1 == 0:
                print(erros)
        
        historico_erro = []
        for i in historico:
            historico_erro.append(i.get('textcat'))

        historico_erro = numpy.array(historico_erro)

        plt.plot(historico_erro)
        plt.title('Progressão do Erro')
        plt.xlabel('Batches')
        plt.ylabel('Erro')
        plt.show()

        modelo.to_disk('modelo')
    
    def teste_fase(self):
        #Teste com uma fase
        base = pandas.read_csv('/home/egmon/Yandex/Programação/Udemy/Python/Python_para_Financas/Bases_de_Dados/stock_data.csv')
        base_treinamento, base_teste = train_test_split(base, test_size=0.3)
        print(base_teste)
        modelo_carregado = spacy.load('modelo')
        print(modelo_carregado)

        #Texto positivo
        try:
            aux = 0
            if aux == 1:
                aux = int(input('\nValor positivo: '))
                texto_positivo = base_teste['Text'][aux]
                print(texto_positivo)
                previsao = modelo_carregado(texto_positivo)
                print(previsao.cats)

                #Texto negativo
                aux = int(input('\nValor negativo: '))
                texto_negativo = base_teste['Text'][aux]
                print(texto_negativo)
                previsao = modelo_carregado(texto_negativo)
                print(previsao.cats)

        except:
            Clean().clean()
            Tratamento_classe().teste_fase()


        try:
            textos_positivos_string = ' '.join(texto_positivo)
            pln = spacy.load('en_core_web_sm')

            def preprocessamento(texto):
                texto = texto.lower()
                texto = re.sub(r'@[A-Za-z0-9$-_@.&+]+', ' ', texto)
                texto = re.sub(r'https?://[A-Za-z0-9./_]+', ' ', texto)
                texto = re.sub(r' +', ' ', texto)

                documento = pln(textos_positivos_string)
                Lista_b = []
                for token in documento:
                    Lista_b.append(token.lemma_)

                Lista_b = [palavra for palavra in Lista_b if palavra not in stop_words and palavra not in string.punctuation]
                Lista_b = ' '.join([str(elemento) for elemento in Lista_b if not elemento.isdigit()])

                return Lista_b

            texto_positivo = 'AAP over 451 could start an ankle grabbing session 0_o'
            texto_positivo = preprocessamento(texto_positivo)
            print(texto_positivo)
        except:
            print('\nDeu ruim')


        #Avaliação do modelo
        previsoes = []
        for i in base_teste['Text']:
            #print(i)
            previsao = modelo_carregado(i)
            previsoes.append(previsao.cats)
        print(previsoes[0:5])

        previsoes_final = []
        for i in previsoes:
            if i['POSITIVO'] > i['NEGATIVO']:
                previsoes_final.append(1)
            else:
                previsoes_final.append(-1)
        previsoes_final = numpy.array(previsoes_final)
        print('\nprevisoes_final array\n',previsoes_final, numpy.unique(previsoes_final))

        respostas_reais = base_teste['Sentiment'].values
        print(respostas_reais)

        print(accuracy_score(respostas_reais, previsoes_final))

        CM = confusion_matrix(respostas_reais, previsoes_final)
        print(CM)

        sns.heatmap(CM, annot=True)
        #plt.show()

        print(classification_report(respostas_reais, previsoes_final))