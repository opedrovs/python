# Minha solução
matriz = [[], [], []]
somapares = somaterceira = maiorsegunda = 0
for cont in range(0, 3):
    for pos in range(0, 3):
        matriz[cont].append(int(input(f'Digite um valor para [{cont}, {pos}]: ')))
print('-=' * 30)
for lista in matriz:
    print(f'[ {lista[0]:^3} ][ {lista[1]:^3} ][ {lista[2]:^3} ]')
    for item in lista:
        if item % 2 == 0:
            somapares += item
    somaterceira += lista[2]
    maiorsegunda = max(matriz[1])
print('-=' * 30)
print(f'A soma dos valores pares é {somapares}')
print(f'A soma dos valores da terceira coluna é {somaterceira}.')
print(f'O maior valor da segunda linha é {maiorsegunda}.')
