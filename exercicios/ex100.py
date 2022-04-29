from time import sleep
from random import randint

cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

# Minha solução


def sorteia(valores):
    for cont in range(0, 5):
        valores.append(randint(1, 10))
    print(f'Sorteando {az}{len(valores)}{li} valores da lista: ', end='')
    for valor in valores:
        print(f'{am}{valor}{li} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somaPar(valores):
    soma = 0
    for valor in valores:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {az}{valores}{li}, temos {vd}{soma}{li}')


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
