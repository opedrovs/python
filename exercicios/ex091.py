from random import randint
from time import sleep
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
print('Valores sorteados:')
for jogador, valor in jogadores.items():
    print(f'{jogador} tirou {valor} no dado.')
    sleep(1)
print('-=' * 30)
