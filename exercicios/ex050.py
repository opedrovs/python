soma = 0
for cont in range(1, 7):
    num = int(input(f'Digite o {cont}º valor: '))
    if num % 2 == 0:
        soma += num
print(f'A soma de todos os valores pares é de {soma}')
