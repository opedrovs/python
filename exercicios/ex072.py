cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
'''
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num > 20 or num < 0:
    num = int(input(f'{vm}Tente novamente.{li} Digite um número entre 0 e 20: '))
print(f'Você digitou o número {am}{extenso[num]}{li}')
'''

# Outra Solução (Guanabara que pediu)
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num > 20 or num < 0:
        num = int(input(f'{vm}Tente novamente.{li} Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {am}{extenso[num]}{li}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim do programa. Volte sempre!')

# Solução Gustavo Guanabara
'''
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[núm]}')
'''
