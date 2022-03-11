# Minha solução

cores = {
    'limpar': '\033[m',
    'vermel': '\033[0;31m',
    'amarelo': '\033[0;33m'
}

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
tot = (dias * 60) + (km * 0.15)
print('{}O total a pagar é de {}{}R${:.2f}{}'.format(cores['vermel'], cores['limpar'], cores['amarelo'], tot, cores['limpar']))

# Solução Gustavo Guanabara (CursoemVideo)
# dias = int(input('Quantos dias alugados? '))
# km = float(input('Quantos Km rodados? '))
# pago = (dias * 60) + (km * 0.15)
# print('O total a pagar é de R${:.2f}'.format(pago))
