from random import randint
cont = maior = menor = 0
print(f'Os valores sorteados foram: ', end='')
for sorteio in range(0, 5):
    sorteado = (randint(1, 10))
    print(f'{sorteado} ', end='')
    cont += 1
    if cont == 1:
        maior = sorteado
        menor = sorteado
    else:
        if maior < sorteado:
            maior = sorteado
        if menor > sorteado:
            menor = sorteado
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
