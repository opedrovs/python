cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'amarelo': '\033[0;33m'
}
l = cores['limpar']
vm = cores['vermelho']
am = cores['amarelo']

num = int(input('Digite um número: '))
divisivel = 0
for cont in range(1, num+1):
    if num % cont == 0:
        print(f'{am}{cont}{l}', end=' ')
        divisivel += 1
        if divisivel > 1 and divisivel <= 2:
            primo = 'É PRIMO'
        else:
            primo = 'NÃO É PRIMO'
    else:
        print(f'{vm}{cont}{l}', end=' ')
print(f'\nO número {num} foi divisível {divisivel} vezes')
print(f'E por isso ele {primo}!')
