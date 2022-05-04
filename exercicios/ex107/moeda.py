def metade(preco):
    res = preco / 2
    return res


def dobro(preco):
    res = preco * 2
    return res


def aumentar(preco, porc):
    res = preco + (preco / 100) * porc
    return res


def diminuir(preco, porc):
    res = preco - (preco / 100) * porc
    return res


# Solução Gustavo Guanabara


'''def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço, taxa):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res'''
