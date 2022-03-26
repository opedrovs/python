contin = 'S'
totnum = 0
somanum = 0
media = 0
lista = []
while contin == 'S':
    num = int(input('Digite um número: '))
    contin = str(input('Quer continuar? [S/N] ')).upper()
    totnum += 1
    somanum += num
    media = somanum / totnum
    lista += [num]
print(f'Você digitou {totnum} números e a média foi {media:.2f}')
print(f'O maior valor foi {max(lista)} e o menor foi {min(lista)}')
