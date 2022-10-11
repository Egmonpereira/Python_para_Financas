import numpy
import pandas
import plotly.express as px
import random

from capm_preparacao import Preparacao
from graficos import Grafico_Capm

class Capm(object):
    def __init__(self,Lista_Aux):
        self.Lista_Aux = Lista_Aux

    def capm(self):
        print('\n:::CAPM:::\n')
        def visualiza_betas_alphas(Betas, Alphas):
            Aux = []
            print('\nVisualização dos Betas e Alphas')
            for i, ativo in enumerate(P.columns[0:-1]):
                Aux.append([ativo, Betas[i], Alphas[i]])
            Ativos = pandas.DataFrame(Aux,columns=['Ações','Beta','Alpha'])
            print(Ativos)

        def visualiza_capm(capm):
            Aux = []
            print('\nVisualização dos CAPMs')
            for i, ativo in enumerate(P.columns[0:-1]):
                Aux.append([ativo, capm[i] * 100])
            Ativos = pandas.DataFrame(Aux,columns=['Ações','CAPM'])
            print(Ativos)

        P = Preparacao.preparacao(self)
        #Grafico_Capm(P).grafico_Capm()

        Aux = []
        print('Escolha as Ações a serem comparadas:')
        for i in self.Lista_Aux:
            print('Inserir',i,'S/N? ',end='')
            s = 's'#input().lower()
            if s == 's':
                Aux.append('MAGALU')#i)
                Aux.append('BOVA')
                if len(Aux) == 2:
                    break
        
        if len(Aux) != 2:
            print('Uma ou mais Ação deixou de ser adicionada.')
            while len(Aux) < 2:
                temp = random.randint(1,5)
                Aux.append(self.Lista_Aux[temp])
                if len(Aux) == 2:
                    if Aux[0] == Aux[1]:
                        Aux.pop()
            print('As Ações ',Aux[0],' e ',Aux[1],' foram inseridas')

        beta, alpha = numpy.polyfit(x = P[Aux[0]], y = P[Aux[1]], deg = 1)
        print('Beta:',beta,'\nAlpha:',alpha,'\nAlpha: %.02f ' %(alpha * 10000),'%')
        #Beta diz quão volátil é a ação da empresa no y.
        #Alpha mostra o excesso de retorno. Se alpha > 0 é bom.
        #Grafico_Capm(P, beta, alpha).grafico_Capm()

        #A covariância é o processo antes de se fazer o cálculo do coeficiente de correlação para medir a direção que dois ativos estão apontando
        #matriz_covariancia = P.drop(columns=['GOL','CVC','WEGE','TOTS']).cov()
        #print(matriz_covariancia)
        #Calculando o coeficiênte de correlação
        #matriz_covariancia = P.drop(columns=['GOL','CVC','WEGE','TOTS']).corr()
        #print(matriz_covariancia)
        #Covariância anual
        matriz_covariancia = P.drop(columns=[self.Lista_Aux[0],self.Lista_Aux[1],self.Lista_Aux[2],self.Lista_Aux[3]]).cov() * 246
        print('\n',matriz_covariancia)
        cov_magalu_bova = matriz_covariancia.iloc[0,1]
        print('Covariância ',Aux[0],' X ',Aux[1],':',cov_magalu_bova)
        variancia_bova = P[self.Lista_Aux[5]].var() * 246
        print(variancia_bova)
        beta_magalu = cov_magalu_bova / variancia_bova
        print(beta_magalu)

        #Cálculo do retorno esperado (Rm) e retorno sem risco (Rf)
        rm = P[self.Lista_Aux[4]].mean() * 246
        print('\nRetorno esperado:',rm)
        taxa_selic_historico = numpy.array([12.75, 14.25, 12.25, 6.5, 5.0, 2.0])
        rf = taxa_selic_historico.mean() / 100
        print(rf)

        #Calculando o CAPM - quem investir nesta ação ganhará esta porcentagem pelo risco de invertir nela
        capm_magalu = rf + (beta * (rm - rf))
        print('\nCAPM ',Aux[0],': %.2f' %(capm_magalu * 100),'%')

        Betas = []
        Alphas = []
        for ativo in P.columns[0:-1]:
            #print(ativo)
            beta, alpha = numpy.polyfit(P[Aux[1]],P[ativo], 1)
            Betas.append(beta)
            Alphas.append(alpha)
        #print(Betas,Alphas)

        visualiza_betas_alphas(Betas,Alphas)

        #O quanto a carteira excedeu a Bova ou não
        print('\nComparando o rendimento da carteira com a ',Aux[1],':\n',numpy.array(Alphas).mean() * 1000)

        capm_empresas = []
        for i, ativo in enumerate(P.columns[0:-1]):
            capm_empresas.append(rf + (Betas[i] * (rm - rf)))
        
        visualiza_capm(capm_empresas)

        pesos = numpy.array([0.2, 0.2, 0.2, 0.2, 0.2])
        capm_portifolio = numpy.sum(capm_empresas * pesos) * 100
        print('\nGanho ou perca pelo risco de investir no Portifólio: %.02f' %capm_portifolio,'%')

