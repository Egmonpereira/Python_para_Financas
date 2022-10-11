from clean import Clean
from facebookprophet import Fbprophet
from classifica_empresas import Classifica_Empresas
from dados import Dados
from acoesgerais import AcoesGerais
from datetime import date

if __name__ == "__main__":
    Clean.clean('self')
    #Lista = ['ABEV3.SA','ODPV3.SA','VIVT3.SA','PETR3.SA','BBAS3.SA','BOVA11.SA']
    #Lista_Aux = ['AMBEV','ODONTOPREV','VIVO','PETROBRAS','BBRASIL','BOVA']
    s = 'n'#input('Entrar com dados? S/N: ').lower()
    Lista, Lista_Aux, name, Sai = Dados(s).dados()
    
    try:       
        a = AcoesGerais(Lista,Lista_Aux)
        with open('Data.txt', 'r') as Data:
            data = Data.read()
        if data != str(date.today()):
            with open('Data.txt', 'w') as Data:
                Data.write(str(date.today()))
            print("Importando dados das Acoes\n ",Lista_Aux)
            a.acoesGerais()
        else:
            print("Dados atualizados em",data)
    except Exception as erro:
        print(erro)
        print('Nenhuma Lista selecionada!')

    #Fbprophet(Lista, Lista_Aux, name, Sai).facebookprophet() 
    Classifica_Empresas().classifica_empresas()