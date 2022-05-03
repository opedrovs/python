from ex108 import moeda

cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}
limpar = cores['limpar']
vermelho = cores['vermelho']
verde = cores['verde']
amarelo = cores['amarelo']

p = float(input(f'Digite o preço: {amarelo}R${limpar}'))
print(f'A metade de {moeda.moeda(p)} é {vermelho}{moeda.moeda(moeda.metade(p))}{limpar}')
print(f'O dobro de {moeda.moeda(p)} é {verde}{moeda.moeda(moeda.dobro(p))}{limpar}')
print(f'Reduzindo 13%, temos {vermelho}{moeda.moeda(moeda.diminuir(p, 13))}{limpar}')
print(f'Aumentando 10%, temos {verde}{moeda.moeda(moeda.aumentar(p, 10))}{limpar}')
