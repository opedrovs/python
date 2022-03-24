# Minha solução
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'amarelo': '\033[0;33m',
    'verde': '\033[0;32m'
}
l = cores['limpar']
vm = cores['vermelho']
am = cores['amarelo']
vd = cores['verde']

num = int(input('Digite um número: '))
divisivel = 0
primo = ''
for cont in range(1, num+1):
    if num % cont == 0:
        print(f'{am}{cont}{l}', end=' ')
        divisivel += 1
        if divisivel == 2:
            # Se o número é PRIMO
            primo = f'{vd}É PRIMO{l}'
        else:
            # Se o número NÃO é PRIMO
            primo = f'{vm}NÃO É PRIMO{l}'
    else:
        print(f'{vm}{cont}{l}', end=' ')
print(f'\nO número {num} foi divisível {divisivel} vezes')
print(f'E por isso ele {primo}!')

# Solução Gustavo Guanabara:
'''
núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
'''
