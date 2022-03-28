# Minha solução
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']

casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
mensal = casa / (anos * 12)
print(f'Para pagar uma casa de {vm}R${casa:.2f}{li} em {am}{anos} anos{li} a prestação será de {vd}R${mensal:.2f}{li}')
if mensal <= (sal * 30 / 100):
    print(f'{vd}Empréstimo pode ser {am}CONCEDIDO{vd}!{li}')
else:
    print(f'{vm}Empréstimo {am}NEGADO{vm}!{li}')

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
