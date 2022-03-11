from random import choice
from time import sleep
# Minha solução
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

print('Suas opções:')
print(f'[ {rx}0{l} ] PEDRA')
print(f'[ {rx}1{l} ] PAPEL')
print(f'[ {rx}2{l} ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
jogadas = ['Pedra', 'Papel', 'Tesoura']
computador = choice(jogadas)
if jogador >= 3:
    print(f'{vm}[ERRO] Jogada inválida!{l}')
elif jogador == 0:
    # Caso o jogador jogue PEDRA
    jogador = 'Pedra'
    if computador == 'Tesoura':
        # Jogador vencedor
        vencedor = f'{vd}VENCE JOGADOR{l}'
    elif computador == 'Papel':
        # Computador vencedor
        vencedor = f'{vm}VENCE COMPUTADOR{l}'
    elif computador == jogador:
        # Empate
        vencedor = f'{am}HOUVE UM EMPATE{l}'
    print(f'{az}-={l}' * 12)
    print(f'Jogador jogou {am}{jogador}{l}')
    print(f'Computador jogou {am}{computador}{l}')
    print(f'{az}-={l}' * 12)
    print(vencedor)
elif jogador == 1:
    # Caso o jogador jogue PAPEL
    jogador = 'Papel'
    if computador == 'Pedra':
        # Jogador vencedor
        vencedor = f'{vd}VENCE JOGADOR{l}'
    elif computador == 'Tesoura':
        # Computador vencedor
        vencedor = f'{vm}VENCE COMPUTADOR{l}'
    elif computador == jogador:
        # Empate
        vencedor = f'{am}HOUVE UM EMPATE{l}'
    print(f'{az}-={l}' * 12)
    print(f'Jogador jogou {am}{jogador}{l}')
    print(f'Computador jogou {am}{computador}{l}')
    print(f'{az}-={l}' * 12)
    print(vencedor)
elif jogador == 2:
    # Caso o jogador jogue TESOURA
    jogador = 'Tesoura'
    if computador == 'Papel':
        # Jogador vencedor
        vencedor = f'{vd}VENCE JOGADOR{l}'
    elif computador == 'Pedra':
        # Computador vencedor
        vencedor = f'{vm}VENCE COMPUTADOR{l}'
    elif computador == jogador:
        # Empate
        vencedor = f'{am}HOUVE UM EMPATE{l}'
    print(f'{az}-={l}' * 12)
    print(f'Jogador jogou {am}{jogador}{l}')
    print(f'Computador jogou {am}{computador}{l}')
    print(f'{az}-={l}' * 12)
    print(vencedor)
