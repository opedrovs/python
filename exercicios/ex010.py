# A cotação atual de 24/02/2022 é de R$ 5.105

cotacao = float(input('Antes de mais nada, quanto está a cotação do Dólar? '))
reais = float(input('Quantos R$ você tem na carteira? '))
usd = reais / cotacao
print('Com R$ {:.2f} você pode comprar US$ {:.2f}!'.format(reais, usd))
