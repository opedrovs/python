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

# Minha solução
contin = 'S'
totnum = 0
somanum = 0
media = 0
lista = []
menor = maior = 0
while contin == 'S':
    num = int(input(f'Digite um número: '))
    contin = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).upper().strip()
    totnum += 1
    somanum += num
    lista += [num]
    maior = max(lista)
    menor = min(lista)
media = somanum / totnum
if totnum == 1:
    print(f'Você digitou {az}{totnum}{li} número e a média foi {am}{media:.2f}{li}')
else:
    print(f'Você digitou {az}{totnum}{li} números e a média foi {am}{media:.2f}{li}')
print(f'O maior valor foi {vd}{maior}{li} e o menor foi {vm}{menor}{li}')

# Solução Gustavo Guanabara
'''
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
'''
