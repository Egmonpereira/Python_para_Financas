from clean import Clean
from analise_sentimentos import Analise_Sentimentos

if __name__ == "__main__":
    Clean.clean('self')

    print('Analise Sentimentos:')
    print(Analise_Sentimentos().analise_sentimentos())

