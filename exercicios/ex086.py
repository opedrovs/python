cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
am = cores['amarelo']
az = cores['azul']

# Minha solução

matriz = [[], [], []]
for linha in range(0, 3):
    for col in range(0, 3):
        matriz[linha].append(int(input(f'Digite um valor para {az}[{linha}, {col}]{li}: ')))
print('-=' * 30)
for lista in matriz:
    print(f'{az}[ {am}{lista[0]:^5} {az}][ {am}{lista[1]:^5} {az}][ {am}{lista[2]:^5} {az}]{li}')

# Solução Gustavo Guanabara
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{c}, {l}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
'''
