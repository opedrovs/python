# Minha solução
valores = [[], []]
for cont in range(1, 8):
    valor = int(input(f'Digite o {cont}º valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print('-=' * 30)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
