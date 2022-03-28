cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
am = cores['amarelo']
rx = cores['roxo']

# Minha solução
from random import shuffle
pri = input('{}Primeiro aluno:{} '.format(rx, li))
seg = input('{}Segundo aluno:{} '.format(rx, li))
ter = input('{}Terceiro aluno:{} '.format(rx, li))
qua = input('{}Quarto aluno:{} '.format(rx, li))
lista = [pri, seg, ter, qua]
shuffle(lista)
print('A ordem de apresentação será \n{}.'.format(lista))

# Outra solução
'''
from random import sample
pri = input('Primeiro aluno: ')
seg = input('Segundo aluno: ')
ter = input('Terceiro aluno: ')
qua = input('Quarto aluno: ')
lista = sample([pri, seg, ter, qua], 4)
print('A ordem de apresentação será \n{}'.format(lista))
'''
# Com sample, podemos limitar o número de pessoas que irão apresentar da lista, no qual colocamos o número 4.
# Por ter quatro pessoas, mas podemos colocar 10 pessoas, nós quais apenas 5 pessoas aleatóriamente irão apresentar.

# Solução Gustavo Guanabara
'''
from random import shuffle
n1 = str(input('Primerio aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)
'''
