cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
l = cores['limpar']
am = cores['amarelo']
az = cores['azul']

# Minha solução:
num = int(input('Digite um número para ver sua tabuada: '))
for cont in range(1, 11):
    print(f'{am}{num} {az}x {cont:2} = {num*cont}{l}')

# Outra solução, onde coloca limite de final:
'''
num = int(input('Digite um número para ver sua tabuada: '))
fim = int(input('Até que linha quer ter na tabuada: '))

for cont in range(1, fim + 1):
    print(f'{num} x {cont:2} = {num * cont}')
'''

# Solução Gustavo Guanabara:
'''
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
'''
