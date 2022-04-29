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
            print(f'{cont}', end='')
            print(' x ' if cont > 1 else ' = ', end='')
    return fat


# Programa Principal
print('-' * 30)
print(fatorial(5, True))
help(fatorial)
