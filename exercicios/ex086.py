# Minha solução
matriz = [[], [], []]
for cont in range(0, 3):
    for pos in range(0, 3):
        matriz[cont].append(int(input(f'Digite um valor para [{cont}, {pos}]: ')))
print('-=' * 30)
for lista in matriz:
    print(f'[ {lista[0]:^3} ][ {lista[1]:^3} ][ {lista[2]:^3} ]')
