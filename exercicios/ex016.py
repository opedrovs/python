# Minha solução
from math import trunc
num = float(input('Digite um número: '))
inteiro = trunc(num)
print('O número {} tem a parte inteira {}.'.format(num, inteiro))

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
