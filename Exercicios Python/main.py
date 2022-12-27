import random
from clean import Clean
from exercicios01 import Exercicio01
from exercicios02 import Exercicio02
from exercicios03 import Exercicio03
from exercicios04 import Exercicio04
from exercicios05 import Exercicio05
from exercicios06 import Exercicio06
from exercicios07 import Exercicio07

if __name__ == "__main__":
    Clean().clean()
    Exercicio01().exe01()
    Exercicio01().viagem()

    Exercicio02().exe02()

    Exercicio03().exe03()

    Exercicio04().exe04()

    Exercicio05().exe05()

    Exercicio06().exe06()

    Nome = "Pedro"
    N1 = random.randint(0,100)
    N2 = random.randint(0,100)
    Exercicio07(Nome, N1, N2).aluno01()

    Nome = "Maria"
    N1 = random.randint(0,100)
    N2 = random.randint(0,100)
    Exercicio07(Nome, N1, N2).aluno01()
