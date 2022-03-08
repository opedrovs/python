# Minha solução
from math import trunc

cores = {
    'limpar': '\033[m',
    'amarel': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}

num = float(input('{}Digite um número: {}'.format(cores['roxo'], cores['limpar'])))
inteiro = trunc(num)
print('{}O número {}{}{}{} tem a parte inteira {}{}{}'.format(cores['azul'], cores['amarel'], num, cores['limpar'], cores['azul'], cores['amarel'], inteiro, cores['limpar']))

# Solução de Gustavo Guanabara
'''
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
'''

# OU

'''
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
'''
