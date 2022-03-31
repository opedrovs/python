cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'cinza': '\033[0;37m'
}
li = cores['limpar']
am = cores['amarelo']
az = cores['azul']
cz = cores['cinza']

# Minha solução após ver a resposta
num = int(input('Digite um número para \ncalcular seu Fatorial: '))
cont = num
fat = 1
print(f'Calculando {az}{num}!{li} {cz}= ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(f'{am}{fat}{li}')


# Minha solução
'''
num = int(input('Digite um número para \ncalcular seu Fatorial: '))
fat = 1
ordem = 2
print(f'Calculando {az}{num}!{li} {cz}=', end=' ')
while num >= ordem:
    print(f'{num}', end=' x ')
    fat *= num
    num -= 1
print(f'1 = {am}{fat}{li}')
'''

# Minha solução utilizando o FOR
'''
num = int(input('Digite um número para \ncalcular seu Fatorial: '))
c = num
f = 1
print(f'Calculando {num}! = ', end='')
for c in range(c, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f'{f}')
'''

# Solução Gustavo Guanabara
# Solução 1
'''
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
'''

# Solução 2
'''
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
'''
