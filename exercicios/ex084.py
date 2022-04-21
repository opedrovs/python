# Minha solução
pessoas = []
dado = []
maior = menor = cont = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    resp = ' '
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
for p in pessoas:
    if cont == 0:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        if p[1] < menor:
            menor = p[1]
    cont += 1
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()
