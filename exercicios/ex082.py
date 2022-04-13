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
    while resp not in 'SN':
        resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).strip().upper()
    if resp == 'N':
        break
for num in numeros:
    if num % 2 == 0:
        pares += [num]
    else:
        impares += [num]
print('-=' * 30)
print(f'A lista completa é {am}{numeros}{li}')
print(f'A lista de pares é {az}{pares}{li}')
print(f'A lista de ímpares é {az}{impares}{li}')
