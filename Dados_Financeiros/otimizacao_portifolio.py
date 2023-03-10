import numpy
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose 
import time
import pandas

from alocacao_ativos import Alocacao_Ativos 

class Otimizacao_Portifolio(object):
    def __init__(self,dataset, dinheiro_total, sem_risco):
        self.dataset = dataset 
        self.dinheiro_total = dinheiro_total
        self.sem_risco = sem_risco
    
    def otimizacao_portifolio(self):
        print('\n:::OTIMIZAÇÃO PORTIFOLIO:::\n')
        numpy.random.seed(10)
        pesos = numpy.random.random(len(self.dataset.columns) - 1)
        pesos = pesos / pesos.sum()
        
        #Função de custo
        def fitness_function(solucao):
            dataset = self.dataset.copy()
            pesos = solucao / solucao.sum()
        
            for i in dataset.columns[1:]:
                dataset[i] = (dataset[i] / dataset[i][0])
                
            for i, acao in enumerate(dataset.columns[1:]):
                dataset[acao] = dataset[acao] * pesos[i] * self.dinheiro_total
                
            dataset.drop(labels = ['Date'], axis = 1, inplace = True)
            dataset['Soma Valores'] = dataset.sum(axis = 1)
            dataset['Taxa de Retorno'] = 0.0
            
            for i in range(1, len(dataset)):
                dataset['Taxa de Retorno'][i] = ((dataset['Soma Valores'][i] / dataset['Soma Valores'][i - 1]) - 1) * 100
                
            sharpe_ratio = (dataset['Taxa de Retorno'].mean() - self.sem_risco) / dataset["Taxa de Retorno"].std() * numpy.sqrt(246)
                
            
            return sharpe_ratio
        
        def visualiza_alocacao(solucao):
            colunas = self.dataset.columns[1:]
            
            for i in range(len(solucao)):
                print(colunas[i], solucao[i] * 100)
        
        print('\nSharpe Ratio',fitness_function(pesos),'\n')
        
        visualiza_alocacao(pesos)

        fitness = mlrose.CustomFitness(fitness_function)
        #problema_maximizacao = mlrose.DiscreteOpt #Se for trabalhar com números inteiros
        problema_maximizacao = mlrose.ContinuousOpt(length=6, fitness_fn=fitness, maximize = True, min_val = 0, max_val = 1)
        problema_minimizacao = mlrose.ContinuousOpt(length=6, fitness_fn=fitness, maximize = False, min_val = 0, max_val = 1)

        #Hill Climb
        def hillclimb():
            print('\nHill Climb')
            #Maximizacao - Melhor retorno
            ini = time.time()
            melhor_solucao, melhor_custo = mlrose.hill_climb(problema_maximizacao, random_state=1)
            fim = time.time()
            
            print('\nTempo: ',(fim - ini) / 60)
            print('melhor_solucao: ',melhor_solucao)
            print('melhor_custo: ', melhor_custo,'\n')
            melhor_solucao = melhor_solucao / melhor_solucao.sum()
            print('\nmelhor_solucao: ',melhor_solucao)
            print('Soma melhor_solucao: ',melhor_solucao.sum())

            visualiza_alocacao(melhor_solucao)
            
            sv1 = Alocacao_Ativos(pandas.read_csv('/home/egmon/Yandex/Programacao/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv'), 5000, melhores_pesos = melhor_solucao)
            _, soma_valor, _, _, _, _  = sv1.alocacao_ativos()
            print('\nLucro Máximo: ',soma_valor)
            
            #Minimizacao - menor retorno
            ini = time.time()
            pior_solucao, pior_custo = mlrose.hill_climb(problema_minimizacao, random_state=1)
            fim = time.time()
            
            print('\nTempo: ',(fim - ini) / 60)
            print('pior_solucao: ',pior_solucao)
            print('pior_custo: ', pior_custo,'\n')
            pior_solucao = pior_solucao / pior_solucao.sum()
            print('pior_solucao: ',pior_solucao)
            print('Soma pior_solucao: ',pior_solucao.sum())

            visualiza_alocacao(pior_solucao)
            
            sv2 = Alocacao_Ativos(pandas.read_csv('/home/egmon/Yandex/Programacao/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv'), 5000, melhores_pesos=pior_solucao)
            _, soma_valor, _, _, _, _  = sv2.alocacao_ativos()

            print('\nLucro Mínimo: ',soma_valor)

        def simulate_annealing():
            print('\nSimulate Annealing')            
            ini = time.time()
            melhor_solucao, melhor_custo = mlrose.simulated_annealing(problema_maximizacao, random_state=1)
            fim = time.time()
            print('\nTempo: ',(fim - ini) / 60,'\n')

            print(melhor_solucao,melhor_custo)
            print(melhor_solucao / melhor_solucao.sum())

            visualiza_alocacao(melhor_solucao)
            
            sv1 = Alocacao_Ativos(pandas.read_csv('/home/egmon/Yandex/Programacao/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv'), 5000, melhores_pesos = melhor_solucao)
            _, soma_valor, _, _, _, _  = sv1.alocacao_ativos()
            print('\nLucro Máximo: ',soma_valor)

        def algoritimo_genetico():
            print('\nAlgoritmo Genético')
            problema_maximizacao_ag = mlrose.ContinuousOpt(length=6, fitness_fn=fitness, maximize=True, min_val=0.1, max_val=1)
            ini = time.time()
            melhor_solucao, melhor_custo = mlrose.genetic_alg(problema_maximizacao_ag, random_state=1)
            fim = time.time()
            print('\nTempo: ',(fim - ini) / 60,'\n')

            melhor_solucao = melhor_solucao / melhor_solucao.sum()
            print('\nmelhor_solucao: ',melhor_solucao)
            print('Soma melhor_solucao: ',melhor_solucao.sum())

            visualiza_alocacao(melhor_solucao)
            
            sv1 = Alocacao_Ativos(pandas.read_csv('/home/egmon/Yandex/Programacao/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv'), 5000, melhores_pesos = melhor_solucao)
            _, soma_valor, _, _, _, _  = sv1.alocacao_ativos()
            print('\nLucro Máximo: ',soma_valor)

        #Chamando as funções
'''        hillclimb()
        
        simulate_annealing()

        algoritimo_genetico()'''