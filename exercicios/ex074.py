cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']

# Minha solução
'''
from random import randint
cont = maior = menor = 0
print(f'Os valores sorteados foram: ', end='')
for sorteio in range(0, 5):
    sorteado = (randint(1, 10))
    print(f'{am}{sorteado}{li} ', end='')
    cont += 1
    if cont == 1:
        maior = sorteado
        menor = sorteado
    else:
        if maior < sorteado:
            maior = sorteado
        if menor > sorteado:
            menor = sorteado
print(f'\nO maior valor sorteado foi {vd}{maior}{li}')
print(f'O menor valor sorteado foi {vm}{menor}{li}')
'''

# Solução Gustavo Guanabara
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
