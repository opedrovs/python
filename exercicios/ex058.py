from random import randint
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
rx = cores['roxo']

# Minha solução após ver a resposta:
computador = randint(0, 10)
print('Sou seu computador... \nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print(f'{vm}Menos{li}... Tente mais uma vez.')
        elif jogador < computador:
            print(f'{vd}Mais{li}... Tente mais uma vez.')
if palpites > 1:
    print(f'Acertou com {am}{palpites}{li} tentativas. Parabéns!')
else:
    print(f'Acertou com {am}{palpites}{li} tentativa. Parabéns!')

# Minha solução
'''
print('Sou seu computador...')
pensei = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = ''
tentativa = 0
while pensei != palpite:
    palpite = int(input(f'{rx}Qual é seu palpite?{li} '))
    tentativa += 1
    if pensei > palpite:
        print(f'{vd}Mais{li}... Tente mais uma vez.')
    elif pensei < palpite:
        print(f'{vm}Menos{li}... Tente mais uma vez.')
    elif pensei == palpite:
        print(f'{vd}Acertou com {am}{tentativa}{vd} tentativas. Parabéns!{li}')
'''

# Solução Gustavo Guanabara
'''
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
'''
