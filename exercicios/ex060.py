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
num = int(input('Digite um número para \ncalcular seu Fatorial: '))
fat = 1
ordem = 2
print(f'Calculando {vd}{num}!{li} =', end=' ')
while num >= ordem:
    print(f'{az}{num}', end=' x ')
    fat *= num
    num -= 1
print(f'{az}1 = {am}{fat}{li}')
