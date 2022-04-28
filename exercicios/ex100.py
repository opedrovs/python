from random import randint
lista = []


def sorteia(valores):
    for c in range(0, 5):
        valores.append(randint(1, 10))
    print(f'Sorteando {len(valores)} valores da lista: ', end='')
    for valor in valores:
        print(f'{valor} ', end='')
    print('PRONTO!')


def somaPar(valores):
    soma = 0
    for valor in valores:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {valores}, temos {soma}')


sorteia(lista)
somaPar(lista)
