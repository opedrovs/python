def moeda(preco):
    return f'R${preco:,.2f}'


def metade(preco):
    return preco / 2


def dobro(preco):
    return preco * 2


def aumentar(preco, porc):
    return preco + ((preco / 100) * porc)


def diminuir(preco, porc):
    return preco - ((preco / 100) * porc)
