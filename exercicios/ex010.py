# A cotação do DÓLAR de 24/02/2022 é de R$ 5.105
# A cotação do EURO de 25/02/2022 é de R$ 5.799

# Minha solução

cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}

li = cores['limpar']
v = cores['verde']
am = cores['amarelo']
az = cores['azul']

cotacao = float(input('Antes de mais nada, quanto está a cotação do Dólar? {}US${}'.format(az, li)))
# cotacaoeuro = float(input('Antes de mais nada, quanto está a cotação do Euro? €'))
real = float(input('Quantos R$ você tem na carteira? {}R${}'.format(v, li)))
dolar = real / cotacao
# euro = real / cotacaoeuro
print('Com {}R${:.2f}{} você pode comprar {}US${:.2f}{}!'.format(v, real, li, az, dolar, li))
# print('Com R${:.2f} você pode comprar €{:.2f}!'.format(real, euro))

# Solução Gustavo Guanabara (CursoemVideo)

# real = float(input('Quanto dinheiro você tem na carteira? R$'))
# dolar = real / 3.27
# print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
