# Melhorar
maior = 0
menor = 99999999
for cont in range(1, 6):
    peso = float(input(f'Peso da {cont}º pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso lido foi de {maior:.1f}Kg')
print(f'O menor peso lido foi de {menor:.1f}Kg')


# Outra solução (Após olhar os comentários):
'''
lista = []
for cont in range(1, 6):
    peso = float(input(f'Peso da {cont}º pessoa: '))
    lista += [peso]
print(f'O maior peso lido foi de {max(lista):.1f}Kg')
print(f'O menor peso lido foi de {min(lista):.1f}Kg')
'''
