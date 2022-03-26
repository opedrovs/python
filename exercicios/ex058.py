cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
l = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
rx = cores['roxo']

# Minha solução
from random import randint
print('Sou seu computador...')
pensei = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = ''
tentativa = 0
while pensei != palpite:
    palpite = int(input(f'{rx}Qual é seu palpite?{l} '))
    if pensei > palpite:
        tentativa += 1
        print(f'{vd}Mais{l}... Tente mais uma vez.')
    elif pensei < palpite:
        tentativa += 1
        print(f'{vm}Menos{l}... Tente mais uma vez.')
    if pensei == palpite:
        tentativa += 1
        print(f'{vd}Acertou com {am}{tentativa}{vd} tentativas. Parabéns!{l}')
