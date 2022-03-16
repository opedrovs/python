# Minha solução
'''
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
l = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
rx = cores['roxo']

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print(f'[ {rx}1{l} ] Converter para BINÁRIO')
print(f'[ {rx}2{l} ] Converter para OCTAL')
print(f'[ {rx}3{l} ] Converter para HEXADECIMAL')
base = int(input('Sua opção: '))
if base == 1:
    print(f'{num} convertido para {am}BINÁRIO{l} é igual a {vd}{num:b}{l}')
elif base == 2:
    print(f'{num} convertido para {am}OCTAL{l} é igual a {vd}{num:o}{l}')
elif base == 3:
    print(f'{num} convertido para {am}HEXADECIMAL{l} é igual a {vd}{num:x}{l}')
else:
    print(f'{vm}[ERRO] Conversão inválida!{l}')
'''
# Solução Gustavo Guanabara

# num = int(input('Digite um número inteiro: '))
# print('''Escolha uma das bases para conversão:
# [ 1 ] converter para BINÁRIO
# [ 2 ] converter para OCTAL
# [ 3 ] converter para HEXADECIMAL''')
# opção = int(input('Sua opção: '))
# if opção == 1:
#     print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
# elif opção == 2:
#     print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
# elif opção == 3:
#     print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
