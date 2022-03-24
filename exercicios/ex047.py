cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'vermelho': '\033[0;31m'
}
l = cores['limpar']
am = cores['amarelo']
vm = cores['vermelho']

# Minha solução após ver a resposta:

print('Contagem de 1 a 50, considerando apenas os PARES')
for cont in range(2, 51, 2):
    print(f'{am}{cont}{l}', end=' ')
print(f'{vm}Acabou{l}')

# Minha solução
'''
print('Contagem de 1 a 50, considerando apenas os PARES')
for cont in range(1, 51):
    if cont % 2 == 0:
        print(f'{am}{cont}{l}', end=' ')
print(f'{vm}Acabou{l}')
'''

# Solução Gustavo Guanabara:
'''
for n in range(2, 50, 2):
    print(n, end=' ')
print('Acabou')
'''
