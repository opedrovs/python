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

# Minha solução (Após ver a resposta):
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O {vd}maior{l} peso lido foi de {am}{maior:.1f}Kg{l}')
print(f'O {vm}menor{l} peso lido foi de {am}{menor:.1f}Kg{l}')

# Minha solução (Não a melhor forma)
'''
maior = 0
menor = 9999999 
for cont in range(1, 6):
    peso = float(input(f'Peso da {cont}º pessoa: '))
    lista += [peso]

    if maior < peso:
        maior = peso

    if menor > peso:
        menor = peso

print(f'O maior peso lido foi de {maior:.1f}Kg')
print(f'O menor peso lido foi de {menor:.1f}Kg')
'''

# Outra solução (Após olhar os comentários):
'''
lista = []
for cont in range(1, 6):
    peso = float(input(f'{az}Peso da {am}{cont}º{az} pessoa:{l} '))
    lista += [peso]
print(f'O {vd}maior{l} peso lido foi de {am}{max(lista):.1f}Kg{l}')
print(f'O {vm}menor{l} peso lido foi de {am}{min(lista):.1f}Kg{l}')
'''

# Solução Gustavo Guanabara:
'''
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.1f}Kg'.format(maior))
print('O menor peso lido foi de {:.1f}Kg'.format(menor))
'''
