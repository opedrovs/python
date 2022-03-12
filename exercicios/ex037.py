# Minha solução

cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}

l = cores['limpar']
vd = cores['verde']
am = cores['amarelo']
rx = cores['roxo']

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print(f'[ {rx}1{l} ] Converter para BINÁRIO')
print(f'[ {rx}2{l} ] Converter para OCTAL')
print(f'[ {rx}3{l} ] Converter para HEXADECIMAL')
base = int(input('Sua opção: '))
if base >= 4:
    print('[ERRO] Conversão inválida!')
elif base == 1:
    print(f'{num} convertido para {am}BINÁRIO{l} é igual a {vd}{bin(num)[2:]}{l}')
elif base == 2:
    print(f'{num} convertido para {am}OCTAL{l} é igual a {vd}{oct(num)[2:]}{l}')
else:
    print(f'{num} convertido para {am}HEXADECIMAL{l} é igual a {vd}{hex(num)[2:]}{l}')
