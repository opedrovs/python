cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
l = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

# Minha solução (com laço de repetição):
frase = str(input('Digite uma frase: '))
separa = frase.split()
juntar = ''.join(separa).upper()

for cont in range(len(juntar), 0, -1):
    inverso = juntar[::-cont]
print(f'O inverso de {juntar} é {az}{inverso}{l}')
if juntar == inverso:
    print(f'{vd}Temos um {am}políndromo{vd}!{l}')
else:
    print(f'{vm}A frase digitado não é um {am}políndromo{vm}!{l}')



# Minha solução (sem laço de repetição):
'''
frase = input('Digite uma frase: ')
separa = frase.split()
juntar = ''.join(separa).upper()

inverso = juntar[::-1]
print(f'O inverso de {juntar} é {inverso}')
if juntar == inverso:
    print('Temos um políndromo!')
else:
    print('A frase digitada não é um políndromo!')
'''
