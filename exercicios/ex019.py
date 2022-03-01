# Minha solução
from random import choice
pri = input('Primeiro aluno: ')
seg = input('Segundo aluno: ')
ter = input('Terceiro aluno: ')
qua = input('Quarto aluno: ')
lista = [pri, seg, ter, qua]
escolhido = choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))

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
