from random import randint
from time import sleep

cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m'
}
li = cores['limpar']
am = cores['amarelo']
az = cores['azul']
rx = cores['roxo']
vm = cores['vermelho']
vd = cores['verde']

# Minha solução
print('{}-=-{}'.format(am, li) * 20)
print('{}Vou pensar em um número entre 0 e 5. Tente advinhar...{}'.format(az, li))
print('{}-=-{}'.format(am, li) * 20)
pensei = randint(0, 5) # Faz o computador "PENSAR"
num = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('{}PROCESSANDO...{}'.format(rx, li))
sleep(2)
if num == pensei:
    print('{}PARABÉNS! Você conseguiu me vencer!{}'.format(vd, li))
else:
    print('{}GANHEI! Eu pensei no número {} e não no {}!{}'.format(vm, pensei, num, li))

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
