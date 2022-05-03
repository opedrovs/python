def titulo(txt):
    print('-' * 30)
    print(f'{txt:^30}')
    print('-' * 30)


def dobro(preco=0):
    preco *= 2
    return f'{preco:.2f}'


def metade(preco=0):
    preco /= 2
    return f'{preco:.2f}'


def aumentar(preco=0, aumento=0):
    preco += ((preco / 100) * aumento)
    return f'{preco:.2f}'


def diminuir(preco=0, reducao=0):
    preco -= ((preco / 100) * reducao)
    return f'{preco:.2f}'


def resumo(preco=0, aumento=0, reducao=0):
    titulo('RESUMO DO VALOR')
    print(f'{"Preço analisado:":<18} R${str(preco).replace(".", ",")}')
    print(f'{"Dobro do preço:":<18} R${str(dobro(preco)).replace(".", ",")}')
    print(f'{"Metade do preço:":<18} R${str(metade(preco)).replace(".", ",")}')
    print(f'{f"{aumento}% de aumento:":<18} R${str(aumentar(preco, aumento)).replace(".", ",")}')
    print(f'{f"{reducao}% de redução:":<18} R${str(diminuir(preco, reducao)).replace(".", ",")}')
    print('-' * 30)
