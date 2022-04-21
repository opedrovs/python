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
for cont in range(0, 3):
    for pos in range(0, 3):
        matriz[cont].append(int(input(f'Digite um valor para {az}[{cont}, {pos}]{li}: ')))
print('-=' * 30)
for lista in matriz:
    print(f'{az}[ {am}{lista[0]:^3} {az}][ {am}{lista[1]:^3} {az}][ {am}{lista[2]:^3} {az}]{li}')
