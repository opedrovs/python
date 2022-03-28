cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

contin = 'S'
totnum = 0
somanum = 0
media = 0
lista = []
while contin == 'S':
    num = int(input('Digite um número: '))
    contin = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).upper()
    totnum += 1
    somanum += num
    media = somanum / totnum
    lista += [num]
print(f'Você digitou {az}{totnum}{li} números e a média foi {am}{media:.2f}{li}')
print(f'O maior valor foi {vd}{max(lista)}{li} e o menor foi {vm}{min(lista)}{li}')
