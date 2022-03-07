# Minha solução
from random import randint
print('-=-' * 18)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 18)
pensei = randint(0, 5)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
if num == pensei:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(pensei, num))

# Solução Gustavo Guanabara

