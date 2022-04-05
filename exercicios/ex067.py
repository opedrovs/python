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
'''
num = 0
cont = 1
while num >= 0:
    num = int(input(f'Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{am}{num} {az}x {cont:2} = {num*cont}{li}')
    print('-'*30)
print(f'{vd}PROGRAMA TABUADA ENCERRADO. Volte sempre!{li}')
'''

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
