# Minha solução
cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}
li = cores['limpar']
vd = cores['verde']
am = cores['amarelo']

pri = int(input('Primeiro número: '))
seg = int(input('Segundo número: '))
if pri > seg:
    print(f'O {vd}PRIMEIRO{li} valor é maior')
elif seg > pri:
    print(f'O {vd}SEGUNDO{li} valor é maior')
else:
    print(f'Os dois valores são {am}IGUAIS{li}')

# Solução Gustavo Guanabara
'''
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n1 < n2:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')
'''
