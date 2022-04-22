from random import sample, randint
from time import sleep

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
'''
jogos = []
print(f'{az}-' * 30)
print(f'{am}{"JOGA NA MEGA SENA":^30}')
print(f'{az}-{li}' * 30)
palpite = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{am}{"-=" * 3} {az}{f"SORTEANDO {palpite} JOGOS"} {am}{"-=" * 3}{li}')
for cont in range(1, palpite+1):
    jogos.append(sample(range(1, 60), 6))
    jogos.sort()
    for item in jogos:
        print(f'Jogo {cont}: {item}')
    jogos.clear()
    sleep(1)
print(f'{f"{am}-=" * 5}{f" {az}< BOA SORTE! >{li} "}{f"{am}-=" * 5}{li}')'''

# Solução Gustavo Guanabara
lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA     ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
