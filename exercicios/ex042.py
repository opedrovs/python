# Minha solução
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

a = float(input(f'{az}Primeiro segmento:{l} '))
b = float(input(f'{az}Segundo segmento:{l} '))
c = float(input(f'{az}Terceiro segmento:{l} '))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        forma = 'EQUILÁTERO'
        print(f'{vd}Os segmentos acima {am}PODEM FORMAR{vd} um triângulo {am}{forma}{vd}!{l}')
    elif a == b or a == c or b == c:
        forma = 'ISÓSCELES'
        print(f'{vd}Os segmentos acima {am}PODEM FORMAR{vd} um triângulo {am}{forma}{vd}!{l}')
    else:
        forma = 'ESCALENO'
        print(f'{vd}Os segmentos acima {am}PODEM FORMAR{vd} um triângulo {am}{forma}{vd}!{l}')
else:
    print(f'{vm}Os segmentos acima {am}NÃO PODEM FORMAR{vm} triângulo!{l}')

# Solução Gustavo Guanabara
'''
r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
'''
