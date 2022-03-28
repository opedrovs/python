# Minha solução
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
rx = cores['roxo']

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print(f'[ {rx}1{li} ] Converter para BINÁRIO')
print(f'[ {rx}2{li} ] Converter para OCTAL')
print(f'[ {rx}3{li} ] Converter para HEXADECIMAL')
base = int(input('Sua opção: '))
if base == 1:
    print(f'{num} convertido para {am}BINÁRIO{li} é igual a {vd}{num:b}{li}')
elif base == 2:
    print(f'{num} convertido para {am}OCTAL{li} é igual a {vd}{num:o}{li}')
elif base == 3:
    print(f'{num} convertido para {am}HEXADECIMAL{li} é igual a {vd}{num:x}{li}')
else:
    print(f'{vm}Conversão inválida. Tente novamente!{li}')

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
