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

lista = []
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
