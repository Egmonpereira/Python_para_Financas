import numpy as np 
import pandas as pd
from graficos import Graficos

class Alocacao_Ativos(object):
    def __init__(self,dataset, dinheiro_total, melhores_pesos = []):
        self.dataset = dataset
        self.dinheiro_total = dinheiro_total
        self.melhores_pesos = melhores_pesos
        
    def alocacao_ativos(self):
        print('\n:::ALOCAÇÃO DE ATIVOS:::\n')
        dataset = self.dataset.copy()
        
        pesos = np.random.random(len(dataset.columns) - 1)
        print(pesos, pesos.sum())
        pesos = pesos / pesos.sum()
        print(pesos, pesos.sum())
        
        seed = 0, 
        if seed != 0:
            np.random.seed(seed)
        
        if type(self.melhores_pesos) != int:
            
            if len(self.melhores_pesos) > 0:
                pesos = self.melhores_pesos
            else:
                pesos = np.random.random(len(dataset.columns) - 1)
                pesos = pesos / pesos.sum()
                #print(pesos,pesos.sum())
        
        colunas = dataset.columns[1:]
        for i in colunas:
            dataset[i] = dataset[i] / dataset[i][0]
        
        for i, acao in enumerate(dataset.columns[1:]):
            dataset[acao] = dataset[acao] * pesos[i] * self.dinheiro_total
        
        dataset['Soma valor'] = dataset.sum(axis = 1)
        
        
        dataset['Taxa de Retorno'] = 0.0
        
        for i in range(1,len(dataset)):
            dataset['Taxa de Retorno'][i] = ((dataset['Soma valor'][i]) / (dataset['Soma valor'][i - 1]) -1 ) * 100
        
        acoes_pesos = pd.DataFrame(data = {'Acões': colunas, 'Pesos': pesos * 100})
        
        #print(dataset, datas, acoes_pesos, '\n',dataset.loc[len(dataset) - 1]['Soma valor'])

        g = Graficos('alocacao', dataset)
        g.graficos()
        
        taxa_retorno_acum = dataset.loc[len(dataset) - 1]['Soma valor'] / dataset.loc[0]['Soma valor'] - 1
        
        desvio_padra_taxa_retorno = dataset['Taxa de Retorno'].std()
        
        sharpe_ratio_medio = (dataset['Taxa de Retorno'].mean() / dataset['Taxa de Retorno'].std()) * np.sqrt(246)
        
        print('\nRENDIMENTO RENDA FIXA:\n')
        taxa_selic_2015 = 12.75
        taxa_selic_2016 = 14.25
        taxa_selic_2017 = 12.25
        taxa_selic_2018 = 6.5
        taxa_selic_2019 = 5.0
        taxa_selic_2020 = 2.0
        
        valor_2015 = self.dinheiro_total + (self.dinheiro_total * taxa_selic_2015 / 100)
        print('valor_2015: R$ %.2f' %valor_2015)
        
        valor_2016 = valor_2015 + (valor_2015 * taxa_selic_2016 / 100)
        print('valor_2016: R$ %0.2f' %valor_2016)
        
        valor_2017 = valor_2016 + (valor_2016 * taxa_selic_2017 / 100)
        print('valor_2017: R$ %0.2f' %valor_2017)
        
        valor_2018 = valor_2017 + (valor_2017 * taxa_selic_2018 / 100)
        print('valor_2018: R$ %0.2f' %valor_2018)
        
        valor_2019 = valor_2018 + (valor_2018 * taxa_selic_2019 / 100)
        print('valor_2019: R$ %0.2f' %valor_2019)
        
        valor_2020 = valor_2019 + (valor_2019 * taxa_selic_2020 / 100)
        print('valor_2020: R$ %0.2f' %valor_2020)
        
        taxa_retorno_historico = np.array([taxa_selic_2015, taxa_selic_2016, taxa_selic_2017, taxa_selic_2018, taxa_selic_2019, taxa_selic_2020])
        
        rendimentos = valor_2020 - self.dinheiro_total
        print('\nRendimentos %.2f' %rendimentos)
        
        ir = rendimentos * 15 / 100
        
        print('\nRendimento RF - IR: R$ %.2f' %(valor_2020 - ir))        
        print('\ntaxa_retorno_historico.mean()',taxa_retorno_historico.mean() / 100)
        sharpe_ratio_medio = ((dataset['Taxa de Retorno'].mean() - taxa_retorno_historico.mean() / 100)/ dataset['Taxa de Retorno'].std()) * np.sqrt(246)
        print('\nsharpe_ratio_medio',sharpe_ratio_medio)
        
        print('\nacoes_pesos\n',acoes_pesos)
        print('\nsoma_valor:',dataset.loc[len(dataset) - 1]['Soma valor'])
        print('\ndataset\n',dataset)
        print('\ndesvio_padra_taxa_retorno:',desvio_padra_taxa_retorno)
        print('\ntaxa_retorno_acum:',taxa_retorno_acum)
        print('\nsharpe_ratio_medio:',sharpe_ratio_medio)

        return acoes_pesos, dataset.loc[len(dataset) - 1]['Soma valor'], dataset, desvio_padra_taxa_retorno, taxa_retorno_acum, sharpe_ratio_medio