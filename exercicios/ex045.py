from random import choice, randint
from time import sleep

cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']
rx = cores['roxo']

# Minha solução após ver a resposta:

print(f'''Suas opções:
[ {rx}0{li} ] PEDRA
[ {rx}1{li} ] PAPEL
[ {rx}2{li} ] TESOURA''')
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if jogador < 0 or jogador >= 3:
    print(f'{vm}JOGADA INVÁLIDA!{li}')
elif computador == 0:
    print('-=' * 11)
    print(f'Computador jogou {am}{itens[computador]}{li}')
    print(f'Jogador jogou {am}{itens[jogador]}{li}')
    print('-=' * 11)
    if jogador == 0:
        print(f'{am}EMPATE{li}')
    elif jogador == 1:
        print(f'{vd}VENCE JOGADOR{li}')
    elif jogador == 2:
        print(f'{vm}VENCE COMPUTADOR{li}')
elif computador == 1:
    print('-=' * 11)
    print(f'Computador jogou {am}{itens[computador]}{li}')
    print(f'Jogador jogou {am}{itens[jogador]}{li}')
    print('-=' * 11)
    if jogador == 0:
        print(f'{vm}VENCE COMPUTADOR{li}')
    elif jogador == 1:
        print(f'{am}EMPATE{li}')
    elif jogador == 2:
        print(f'{vd}VENCE JOGADOR{li}')
elif computador == 2:
    print('-=' * 11)
    print(f'Computador jogou {am}{itens[computador]}{li}')
    print(f'Jogador jogou {am}{itens[jogador]}{li}')
    print('-=' * 11)
    if jogador == 0:
        print(f'{vd}VENCE JOGADOR{li}')
    elif jogador == 1:
        print(f'{vm}VENCE COMPUTADOR{li}')
    elif jogador == 2:
        print(f'{am}EMPATE{li}')

# Minha primeira solução (sem ver a resposta)

'''
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
    # Jogador jogou PEDRA
    jogador = 'Pedra'
    if computador == 'Tesoura':
        # Jogador vencedor
        vencedor = f'{vd}VENCE JOGADOR{l}'
    elif computador == 'Papel':
        # Computador vencedor
        vencedor = f'{vm}VENCE COMPUTADOR{l}'
    elif computador == jogador:
        # Empate
        vencedor = f'{am}EMPATE{l}'
    print(f'-=' * 12)
    print(f'Computador jogou {am}{computador}{l}')
    print(f'Jogador jogou {am}{jogador}{l}')
    print(f'-=' * 12)
    print(vencedor)
elif jogador == 1:
    # Jogador jogou PAPEL
    jogador = 'Papel'
    if computador == 'Pedra':
        # Jogador vencedor
        vencedor = f'{vd}VENCE JOGADOR{l}'
    elif computador == 'Tesoura':
        # Computador vencedor
        vencedor = f'{vm}VENCE COMPUTADOR{l}'
    elif computador == jogador:
        # Empate
        vencedor = f'{am}EMPATE{l}'
    print(f'-=' * 12)
    print(f'Computador jogou {am}{computador}{l}')
    print(f'Jogador jogou {am}{jogador}{l}')
    print(f'-=' * 12)
    print(vencedor)
elif jogador == 2:
    # Jogador jogou TESOURA
    jogador = 'Tesoura'
    if computador == 'Papel':
        # Jogador vencedor
        vencedor = f'{vd}VENCE JOGADOR{l}'
    elif computador == 'Pedra':
        # Computador vencedor
        vencedor = f'{vm}VENCE COMPUTADOR{l}'
    elif computador == jogador:
        # Empate
        vencedor = f'{am}EMPATE{l}'
    print(f'-=' * 12)
    print(f'Computador jogou {am}{computador}{l}')
    print(f'Jogador jogou {am}{jogador}{l}')
    print(f'-=' * 12)
    print(vencedor)
'''

# Solução Gustavo Guanabara

# from random import randint
# from time import sleep
# itens = ('Pedra', 'Papel', 'Tesoura')
# computador = randint(0, 2)
# print('''Suas opções:
# [ 0 ] Pedra
# [ 1 ] Papel
# [ 2 ] Tesoura''')
# jogador = int(input('Qual é a sua jogada? '))
# print('JO')
# sleep(1)
# print('KEN')
# sleep(1)
# print('PO!!!')
# print('-='*11)
# print('Computador jogou {}'.format(itens[computador]))
# print('Jogador jogou {}'.format(itens[jogador]))
# print('-='*11)
# if computador == 0:
#     if jogador == 0:
#         print('EMPATE')
#     elif jogador == 1:
#         print('VENCE JOGADOR')
#     elif jogador == 2:
#         print('VENCE COMPUTADOR')
#     else:
#         print('JOGADA INVÁLIDA!')
# elif computador == 1:
#     if jogador == 0:
#         print('VENCE COMPUTADOR')
#     elif jogador == 1:
#         print('EMPATE')
#     elif jogador == 2:
#         print('VENCE JOGADOR')
#     else:
#         print('JOGADA INVÁLIDA!')
# elif computador == 2:
#     if jogador == 0:
#         print('VENCE JOGADOR')
#     elif jogador == 1:
#         print('VENCE COMPUTADOR')
#     elif jogador == 2:
#         print('EMPATE')
#     else:
#         print('JOGADA INVÁLIDA!')
