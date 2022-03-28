cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
am = cores['amarelo']
rx = cores['roxo']

# Minha solução
from random import choice
pri = input('{}Primeiro aluno:{} '.format(rx, li))
seg = input('{}Segundo aluno:{} '.format(rx, li))
ter = input('{}Terceiro aluno:{} '.format(rx, li))
qua = input('{}Quarto aluno:{} '.format(rx, li))
lista = [pri, seg, ter, qua]
escolhido = choice(lista)
print('O aluno escolhido foi {}{}{}.'.format(am, escolhido, li))

# Solução Gustavo Guanabara
'''
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
'''
