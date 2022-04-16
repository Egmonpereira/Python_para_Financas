from clean import Clean
from facebookprophet import Fbprophet
from dados import Dados

if __name__ == "__main__":
    Clean.clean('self')
    #Lista = ['ABEV3.SA','ODPV3.SA','VIVT3.SA','PETR3.SA','BBAS3.SA','BOVA11.SA']
    #Lista_Aux = ['AMBEV','ODONTOPREV','VIVO','PETROBRAS','BBRASIL','BOVA']
    s = 'n'#input('Entrar com dados? S/N: ').lower()
    Lista, Lista_Aux, name, Sai = Dados(s).dados()

    Fbprophet(Lista, Lista_Aux, name, Sai).facebookprophet() 
    