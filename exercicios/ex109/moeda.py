'''def moeda(preco=0):
    return f'R${preco:,.2f}'


def metade(preco=0, form=False):
    res = preco / 2
    if form:
        return f'R${res:,.2f}'
    else:
        return res


def dobro(preco=0, form=False):
    res = preco * 2
    if form:
        return f'R${res:,.2f}'
    else:
        return res


def aumentar(preco=0, porc=0, form=False):
    res = preco + ((preco / 100) * porc)
    if form:
        return f'R${res:,.2f}'
    else:
        return res


def diminuir(preco=0, porc=0, form=False):
    res = preco - ((preco / 100) * porc)
    if form:
        return f'R${res:,.2f}'
    else:
        return res'''


# Solução Gustavo Guanabara


def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
