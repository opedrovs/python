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


def resumo(preco=0, aumento=0, reducao=0):
    titulo('RESUMO DO VALOR')
    print(f'{"Preço analisado:":<18} {amarelo}R${preco:,.2f}{limpar}')
    print(f'{"Dobro do preço:":<18} {verde}R${dobro(preco):,.2f}{limpar}')
    print(f'{"Metade do preço:":<18} {vermelho}R${metade(preco):,.2f}{limpar}')
    print(f'{f"{aumento}% de aumento:":<18} {verde}R${aumentar(preco, aumento):,.2f}{limpar}')
    print(f'{f"{reducao}% de redução:":<18} {vermelho}R${diminuir(preco, reducao):,.2f}{limpar}')
    print(f'{azul}-{limpar}' * 30)
