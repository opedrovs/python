from random import randint
from time import sleep
cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

# Minha solução após ver a resposta
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for pos, valor in enumerate(ranking):
    print(f'   {pos+1}º lugar: {valor[0]} com {valor[1]}.')
    sleep(1)

# Minha solução
'''lista = []
valores = []
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
print('Valores sorteados:')
for jogador, valor in jogadores.items():
    print(f'{jogador}{li} tirou {valor} no dado.')
    sleep(1)
print('-=' * 30)
print(f'  {am}== {az}RANKING DOS JOGADORES {am}=={li}  ')
for chave, dado in jogadores.items():
    valores.clear()
    valores.append(dado)
    valores.append(chave)
    lista.append(valores[:])
lista.sort(reverse=True)
for pos, jogador in enumerate(lista):
    print(f'   {vd}{pos+1}º{li} lugar: {az}{jogador[1]}{li} com {am}{jogador[0]}{li}.')
    sleep(1)'''

# Solução Gustavo Guanabara
'''from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)'''
