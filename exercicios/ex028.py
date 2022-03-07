# Minha solução
from random import randint
from time import sleep
cores = {
    'limpa': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m',
    'vermel': '\033[0;31m',
    'verde': '\033[0;32m'
}
print('{}-=-{}'.format(cores['amarelo'], cores['limpa']) * 20)
print('{}Vou pensar em um número entre 0 e 5. Tente advinhar...{}'.format(cores['azul'], cores['limpa']))
print('{}-=-{}'.format(cores['amarelo'], cores['limpa']) * 20)
pensei = randint(0, 5) # Faz o computador "PENSAR"
num = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('{}PROCESSANDO...{}'.format(cores['roxo'], cores['limpa']))
sleep(2.5)
if num == pensei:
    print('{}PARABÉNS! Você conseguiu me vencer!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}GANHEI! Eu pensei no número {} e não no {}!{}'.format(cores['vermel'], pensei, num, cores['limpa']))

# Solução Gustavo Guanabara
'''
from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
'''
