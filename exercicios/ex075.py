cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']
rx = cores['roxo']

num = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: '))
)
print(f'Você digitou os valores {am}{num}{li}')
if num.count(9) == 1:
    print(f'O valor 9 apareceu {vd}{num.count(9)}{li} vez')
else:
    print(f'O valor 9 apareceu {vd}{num.count(9)}{li} vezes')
if 3 not in num:
    print(f'O valor 3 {vm}não foi digitado em nenhuma posição{li}')
else:
    print(f'O valor 3 apareceu na {az}{num.index(3)+1}º{li} posição')
print(f'Os valores pares digitados foram ', end='')
for c in range(0, len(num)):
    if num[c] % 2 == 0:
        print(f'{rx}{num[c]} {li}', end='')




# Solução Gustavo Guanabara
'''
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
'''
