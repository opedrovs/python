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
for cont in range(0, 3):
    for pos in range(0, 3):
        matriz[cont].append(int(input(f'Digite um valor para {az}[{cont}, {pos}]{li}: ')))
print('-=' * 30)
for lista in matriz:
    print(f'{az}[ {am}{lista[0]:^3} {az}][ {am}{lista[1]:^3} {az}][ {am}{lista[2]:^3} {az}]{li}')
    for item in lista:
        if item % 2 == 0:
            somapares += item
    somaterceira += lista[2]
    maiorsegunda = max(matriz[1])
print('-=' * 30)
print(f'A soma dos valores pares é {vd}{somapares}{li}')
print(f'A soma dos valores da terceira coluna é {az}{somaterceira}{li}.')
print(f'O maior valor da segunda linha é {am}{maiorsegunda}{li}.')
