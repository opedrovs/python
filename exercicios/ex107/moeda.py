def metade(preco):
    preco /= 2
    return preco


def dobro(preco):
    preco *= 2
    return preco


def aumentar(preco, porc):
    preco += (preco / 100) * porc
    return preco


def diminuir(preco, porc):
    preco -= (preco / 100) * porc
    return preco
