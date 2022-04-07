cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

# Minha solução
cont = 1
while True:
    num = int(input(f'Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{am}{num} {az}x {cont:2} = {num*cont}{li}')
    print('-'*30)
print(f'{vd}PROGRAMA TABUADA ENCERRADO. Volte sempre!{li}')

# Solução Gustavo Guanabara
'''
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
'''
