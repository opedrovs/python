# Minha solução
cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}
l = cores['limpar']
vd = cores['verde']
am = cores['amarelo']

pri = int(input('Primeiro número: '))
seg = int(input('Segundo número: '))
if pri > seg:
    print(f'O {vd}PRIMEIRO{l} valor é maior')
elif seg > pri:
    print(f'O {vd}SEGUNDO{l} valor é maior')
else:
    print(f'Os dois valores são {am}IGUAIS{l}')
