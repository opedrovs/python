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
numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = ' '
    while resp != 'S' and resp != 'N':
        resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'A lista completa é {az}{numeros}{li}')
print(f'A lista de pares é {am}{pares}{li}')
print(f'A lista de ímpares é {am}{impares}{li}')

# Solução Gustavo Guanabara
'''
num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
'''
