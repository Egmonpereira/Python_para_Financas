import platform
import os

class Clean(object):
    def __init__(self):
        pass

    def clean(self):
        if platform.system() == 'Linux':
            os.system('clear')
        else:
            os.system('cls')

        print('Você está usando Sistema Operacional:',platform.system())
