cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

# Minha solução
matriz = [[], [], []]
somapares = somaterceira = maiorsegunda = 0
for linha in range(0, 3):
    for col in range(0, 3):
        matriz[linha].append(int(input(f'Digite um valor para {az}[{col}, {linha}]{li}: ')))
print('-=' * 30)
for lista in matriz:
    print(f'{az}[ {am}{lista[0]:^5} {az}][ {am}{lista[1]:^5} {az}][ {am}{lista[2]:^5} {az}]{li}')
    for item in lista:
        if item % 2 == 0:
            somapares += item
    somaterceira += lista[2]
    maiorsegunda = max(matriz[1])
print('-=' * 30)
print(f'A soma dos valores pares é {vd}{somapares}{li}')
print(f'A soma dos valores da terceira coluna é {az}{somaterceira}{li}.')
print(f'O maior valor da segunda linha é {am}{maiorsegunda}{li}.')

# Solução Gustavo Guanabara
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{c}, {l}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
'''
