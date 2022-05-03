def titulo(txt):
    print('-' * 30)
    print(f'{txt:^30}')
    print('-' * 30)


def dobro(preco=0):
    preco *= 2
    return preco


def metade(preco=0):
    preco /= 2
    return preco


def aumentar(preco=0, aumento=0):
    preco += ((preco / 100) * aumento)
    return preco


def diminuir(preco=0, reducao=0):
    preco -= ((preco / 100) * reducao)
    return preco


def resumo(preco, aumento, reducao):
    titulo('RESUMO DO VALOR')
    print(f'{"Preço analisado:":<18} R${preco:,.2f}')
    print(f'{"Dobro do preço:":<18} R${dobro(preco):,.2f}')
    print(f'{"Metade do preço:":<18} R${metade(preco):,.2f}')
    print(f'{f"{aumento}% de aumento:":<18} R${aumentar(preco, aumento):,.2f}')
    print(f'{f"{reducao}% de redução:":<18} R${diminuir(preco, reducao):,.2f}')
    print('-' * 30)
