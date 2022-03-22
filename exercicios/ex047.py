cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'vermelho': '\033[0;31m'
}
l = cores['limpar']
am = cores['amarelo']
vm = cores['vermelho']

# Minha solução
print('Contagem de 1 a 50 dos PARES')
for c in range(1, 51):
    if c % 2 == 0:
        print(f'{am}{c}{l}', end=' ')
print(f'{vm}Acabou{l}')
