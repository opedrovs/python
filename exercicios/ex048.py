valores = 0
soma = 0
for cont in range(0, 501):
    if cont % 2 != 0 and cont % 3 == 0:
        valores += 1
        soma += cont

print(f'A soma de todos os {valores} valores solicitados é {soma}')

