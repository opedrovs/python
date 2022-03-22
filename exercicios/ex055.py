cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
l = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']
rx = cores['roxo']

# Minha solução
'''
maior = 0
menor = 99999999
for cont in range(1, 6):
    peso = float(input(f'Peso da {cont}º pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso lido foi de {maior:.1f}Kg')
print(f'O menor peso lido foi de {menor:.1f}Kg')
'''

# Outra solução (Após olhar os comentários):
lista = []
for cont in range(1, 6):
    peso = float(input(f'{az}Peso da {am}{cont}º{az} pessoa:{l} '))
    lista += [peso]
print(f'O {vd}maior{l} peso lido foi de {am}{max(lista):.1f}Kg{l}')
print(f'O {vm}menor{l} peso lido foi de {am}{min(lista):.1f}Kg{l}')

