def moeda(preco=0):
    return f'R${preco:,.2f}'


def metade(preco=0, form=False):
    preco /= 2
    if form:
        return f'R${preco:,.2f}'
    else:
        return preco


def dobro(preco=0, form=False):
    preco *= 2
    if form:
        return f'R${preco:,.2f}'
    else:
        return preco


def aumentar(preco=0, porc=0, form=False):
    preco += ((preco / 100) * porc)
    if form:
        return f'R${preco:,.2f}'
    else:
        return preco


def diminuir(preco=0, porc=0, form=False):
    preco -= ((preco / 100) * porc)
    if form:
        return f'R${preco:,.2f}'
    else:
        return preco
