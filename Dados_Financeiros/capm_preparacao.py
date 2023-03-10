import pandas

class Preparacao(object):
    def preparacao():
        dataset = pandas.read_csv('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv')
        print(dataset)
        
        dataset.drop(labels=['Date'], axis=1, inplace=True)
        print(dataset)

        dataset_normalizado = dataset.copy()
        for i in dataset.columns:
            dataset_normalizado[i] = dataset[i] / dataset[i][0]
        print(dataset_normalizado)

        dataset_taxa_de_retorno = (dataset_normalizado / dataset_normalizado.shift(1)) - 1
        print(dataset_taxa_de_retorno)
        dataset_taxa_de_retorno.fillna(0, inplace=True)
        print(dataset_taxa_de_retorno.head())

        tx_diaria = dataset_taxa_de_retorno.mean()
        tx_anual = dataset_taxa_de_retorno.mean() * 246
        print('Taxa de Retorno diária\n',tx_diaria)
        print('Taxa de Retorno anual\n',tx_anual)

        return dataset_taxa_de_retorno  
