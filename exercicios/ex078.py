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
valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))
print('=-' * 30)
print(f'Você digitou os valores {am}{valores}{li}')
print(f'O maior valor digitado foi {vd}{max(valores)}{li} nas posições ', end='')
for pos in range(0, len(valores)):
    if valores[pos] == max(valores):
        print(f'{az}{pos}{li}... ', end='')
print(f'\nO menor valor digitado foi {vm}{min(valores)}{li} nas posições ', end='')
for pos in range(0, len(valores)):
    if valores[pos] == min(valores):
        print(f'{az}{pos}{li}... ', end='')

# Solução Gustavo Guanabara
'''
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
'''
