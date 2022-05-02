cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
limp = cores['limpar']
amar = cores['amarelo']
azul = cores['azul']


# Minha solução


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fat = 1
    for cont in range(n, 0, -1):
        fat *= cont
        if show:
            print(f'{azul}{cont}', end='')
            print(' x ' if cont > 1 else ' = ', end='')
    return f'{amar}{fat}{limp}'


# Programa Principal
print('-' * 30)
print(fatorial(5, True))
# help(fatorial)


# Gustavo Guanabara


'''def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
print(fatorial(5, show=True))
help(fatorial)'''
