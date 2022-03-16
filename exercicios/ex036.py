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

casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
mensal = casa / (anos * 12)
print(f'Para pagar uma casa de {vm}R${casa:.2f}{l} em {am}{anos} anos{l} a prestação será de {vd}R${mensal:.2f}{l}')
if mensal <= (sal * 30 / 100):
    print(f'Empréstimo pode ser {vd}CONCEDIDO{l}!')
else:
    print(f'Empréstimo {vm}NEGADO{l}!')

# Solução Gustavo Guanabara
'''
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')
'''
