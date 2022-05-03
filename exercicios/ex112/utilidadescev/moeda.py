cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
limpar = cores['limpar']
vermelho = cores['vermelho']
verde = cores['verde']
amarelo = cores['amarelo']
azul = cores['azul']


def titulo(txt):
    print(f'{azul}-' * 30)
    print(f'{amarelo}{txt:^30}')
    print(f'{azul}-{limpar}' * 30)


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
    print(f'{"Preço analisado:":<18} {amarelo}R${str(preco).replace(".", ",")}{limpar}')
    print(f'{"Dobro do preço:":<18} {verde}R${str(dobro(preco)).replace(".", ",")}{limpar}')
    print(f'{"Metade do preço:":<18} {vermelho}R${str(metade(preco)).replace(".", ",")}{limpar}')
    print(f'{f"{aumento}% de aumento:":<18} {verde}R${str(aumentar(preco, aumento)).replace(".", ",")}{limpar}')
    print(f'{f"{reducao}% de redução:":<18} {vermelho}R${str(diminuir(preco, reducao)).replace(".", ",")}{limpar}')
    print(f'{azul}-{limpar}' * 30)
