# Minha solução
from random import sample
from time import sleep
jogos = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
palpite = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{"-=" * 3} {f"SORTEANDO {palpite} JOGOS"} {"-=" * 3}')
for cont in range(1, palpite+1):
    jogos.append(sample(range(1, 60), 6))
    jogos.sort()
    for item in jogos:
        print(f'Jogo {cont}: {item}')
    jogos.clear()
    sleep(1)
print(f'{"-=" * 5}{" < BOA SORTE! > "}{"-=" * 5}')
