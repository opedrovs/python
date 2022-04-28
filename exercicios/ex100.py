# Minha solução
from time import sleep
from random import randint


def sorteia(valores):
    for cont in range(0, 5):
        valores.append(randint(1, 10))
    print(f'Sorteando {len(valores)} valores da lista: ', end='')
    for valor in valores:
        print(f'{valor} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somaPar(valores):
    soma = 0
    for valor in valores:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {valores}, temos {soma}')


# Programa Principal
lista = list()
sorteia(lista)
somaPar(lista)

# Solução Gustavo Guanabara


'''def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    n = 0
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = list()
sorteia(números)
somaPar(números)'''
