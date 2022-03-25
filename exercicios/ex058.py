# Minha solução
from random import randint
print('Sou seu computador...')
pensei = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = ''
tentativa = 0
while pensei != palpite:
    palpite = int(input('Qual é seu palpite? '))
    if pensei > palpite:
        tentativa += 1
        print('Mais... Tente mais uma vez.')
    elif pensei < palpite:
        tentativa += 1
        print('Menos... Tente mais uma vez.')
    if pensei == palpite:
        tentativa += 1
        print(f'Acertou com {tentativa} tentativas. Parabéns!')
