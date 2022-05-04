'''cores = {
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
    print(f'{azul}-{limpar}' * 30)'''

# Solução Gustavo Guanabara


def aumentar(preço=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação
    :param preço: o preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
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


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    # \t significa tabulação, deixar o código organizado em forma de tabela
    print('-' * 30)
