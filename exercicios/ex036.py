# Minha solução

cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}

l = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']

valorcasa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))
meses = ano*12
mensal = valorcasa / meses
print(f'Para pagar uma casa de {vm}R${valorcasa:.2f}{l} em {am}{ano}{l} anos a prestação será de {vd}R${mensal:.2f}{l}')
if mensal <= (sal * 30 / 100):
    print(f'Empréstimo pode ser {vd}CONCEDIDO{l}!')
else:
    print(f'Empréstimo {vm}NEGADO{l}!')

