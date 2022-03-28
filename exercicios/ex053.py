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

# Minha solução (após ver a resposta):
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {az}{inverso}{li}')
if inverso == junto:
    print(f'{vd}Temos um {am}políndromo{vd}!{li}')
else:
    print(f'{vm}A frase digitada não é um {am}políndromo{vm}!{li}')

# Minha solução (com laço de repetição):
'''
frase = str(input('Digite uma frase: ')).upper().strip()
separado = frase.split()
junto = ''.join(separado)
for cont in range(len(junto), 0, -1):
    inverso = junto[::-cont]
print(f'O inverso de {junto} é {az}{inverso}{li}')
if junto == inverso:
    print(f'{vd}Temos um {am}políndromo{vd}!{li}')
else:
    print(f'{vm}A frase digitada não é um {am}políndromo{vm}!{li}')
'''

# Minha solução (sem laço de repetição):
'''
frase = input('Digite uma frase: ').upper().strip()
separado = frase.split()
junto = ''.join(separado)

inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Temos um políndromo!')
else:
    print('A frase digitada não é um políndromo!')
'''

# Solução Gustavo Guanabara:
'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um políndromo!')
else:
    print('A frase digitada não é um políndromo!')
'''

# OU (outra solução de Gustavo Guanabara)
'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um políndromo!')
else:
    print('A frase digitada não é um políndromo!')
'''
