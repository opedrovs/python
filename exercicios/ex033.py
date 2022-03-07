pri = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
ter = int(input('Terceiro valor: '))

# Maior valor:
if pri > seg and pri > ter:
    maior = pri
elif seg > pri and seg > ter:
    maior = seg
elif ter > pri and ter > seg:
    maior = ter

# Menor valor:
if pri < seg and pri < ter:
    menor = pri
elif seg < pri and seg < ter:
    menor = seg
elif ter < pri and ter < seg:
    menor = ter

print('O menor valor informado foi {}'.format(menor))
print('O maior valor informado foi {}'.format(maior))
