from pandas_datareader import data
import seaborn, pandas, yfinance
from graficos import Graficos 

class AcoesGerais(object):
    def __init__(self,Lista,Lista_Aux):
        self.Lista = Lista
        self.Lista_Aux = Lista_Aux
    
    def retorna(self):
        return self.Lista, self.Lista_Aux
    
    def acoesGerais(self):
        print('\n:::AÇÕES GERAIS:::\n')
        
        for i in self.Lista:
            #acoes_df[i] = data.DataReader(i, data_source = 'yahoo', start = '2015-01-01', end = '2020-11-03')['Close']
            #print("Açoes Gerais i =",i)
            try:
                acoes_df = pandas.DataFrame(data.DataReader(i, data_source = 'yahoo', start = '2015-01-01')['Close'])
                #acoes_df = pd.DataFrame(data.DataReader(i, data_source = 'yahoo', start = '2015-01-01', end = '2020-11-03')['Close'])
            except Exception as e:
                acoes_df = yfinance.Tickers(' '.join(self.Lista))
                print('acoes_df',acoes_df)
                print(e)

        for i in range(len(self.Lista)):
            acoes_df = acoes_df.rename(columns={self.Lista[i]: self.Lista_Aux[i]})
        
        acoes_df.dropna(inplace=True)
        print(acoes_df.isnull().sum())
        print(acoes_df)
        acoes_df.to_csv('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv')
        print(acoes_df.columns[1:])
        print(acoes_df.describe())

#        sns.histplot(acoes_df['GOL'], kde=True)
#        sns.boxplot(x = acoes_df['GOL'])
        
        acoes_df = pandas.read_csv('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv')

        acoes_df_normalizado = acoes_df.copy()
        for i in acoes_df_normalizado.columns[1:]:
            acoes_df_normalizado[i] = acoes_df_normalizado[i] / acoes_df_normalizado[i][0]
        print(acoes_df_normalizado)

        g = Graficos('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesgerais',acoes_df)
        g.graficos()

        g = Graficos('normalizado', acoes_df_normalizado)
        g.graficos()
        
        
        g = Graficos('historico',acoes_df)
        g.graficos()
        
        g = Graficos('historico normalizado',acoes_df_normalizado)
        g.graficos()
        