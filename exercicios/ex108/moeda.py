'''def moeda(preco):
    return f'R${preco:,.2f}'


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
    return res'''

# Solução Gustavo Guanabara


def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço=0):
    res = preço * 2
    return res


def metade(preço=0):
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
