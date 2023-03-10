from clean import Clean
from facebookprophet import Fbprophet
from classifica_empresas import Classifica_Empresas
from dados import Dados
from acoesgerais import AcoesGerais
from datetime import date
from agrupamento_empresas import Agrupamento_Empresas
from analise_sentimentos import Analise_Sentimentos
from otimizacao_portifolio import Otimizacao_Portifolio
from calculo_risco import Calculo_Risco
from tratamento_classe import Tratamento_classe
import time, pandas

if __name__ == "__main__":
    inicio = time.time()
    Clean.clean('self')
    #as duas linhas abaixo ficam em dados
    #with open('Data.txt', 'w') as Data:
        #Data.write(str('2015-01-01'))
    #Lista = ['ABEV3.SA','ODPV3.SA','VIVT3.SA','PETR3.SA','BBAS3.SA','BOVA11.SA']
    #Lista_Aux = ['AMBEV','ODONTOPREV','VIVO','PETROBRAS','BBRASIL','BOVA']

    try:       
        with open('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/Data.txt', 'r') as Data:
            data = Data.read()
        if data != str(date.today()):
            #s = 's'#input('Entrar com dados? S/N: ').lower()
            Lista, Lista_Aux, name, Sai = Dados('s').dados()
            a = AcoesGerais(Lista,Lista_Aux)
            with open('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/Data.txt', 'w') as Data:
                Data.write(str(date.today()))
            print("Importando dados das Acoes\n ",Lista_Aux)
        else:
            Lista, Lista_Aux, name, Sai = Dados('n').dados()
            print("Dados importados em",data)
    except Exception as erro:
        print(erro)
        print('Nenhuma Lista selecionada!')

    print('Linha 38 - Tempo estimnado: 00.26')
    #Fbprophet(name).facebookprophet() 
    print('Linha 40 - Tempo estimnado: 23:33')
    #Classifica_Empresas().classifica_empresas()
    print('Linha 42 - Tempo estimnado: 00:32')
    #Agrupamento_Empresas().agrupamento_empresas()
    print('Linha 46 - Tempo estimnado: ')
    #Analise_Sentimentos().analise_sentimentos()
    print('Linha 48 - Tempo estimnado: 01:74')
    #Tratamento_classe().tratamento_classe()
    print('Linha 50 - Tempo estimnado: ')
    #Tratamento_classe().teste_fase()
    print('Linha 52 - Tempo estimnado: ')
    c = Calculo_Risco(name,Sai)
    taxa_selic_historico = c.calculo_risco()
    Otimizacao_Portifolio(pandas.read_csv('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/acoesGerais.csv'), 5000, taxa_selic_historico.mean() / 100)
    AcoesGerais(Lista, Lista_Aux).acoesGerais()


    fim = time.time()
    with open('/home/egmon/Yandex/Acadêmico/Udemy/Python/Python_para_Financas/Bases_de_Dados/tempoExecucao.txt', 'w') as t:
        t.write(str('Tempo: %0.2f' %((fim - inicio)/60)))
    print('Tempo: %0.2f' %((fim - inicio)/60))