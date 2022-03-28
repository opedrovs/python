# Minha solução
from math import trunc

cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
am = cores['amarelo']
az = cores['azul']
rx = cores['roxo']

num = float(input('{}Digite um número: {}'.format(rx, li)))
inteiro = trunc(num)
print('{}O número {}{}{}{} tem a parte inteira {}{}{}'.format(az, am, num, li, az, am, inteiro, li))

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
