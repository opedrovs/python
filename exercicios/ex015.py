# Minha solução
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'amarelo': '\033[0;33m'
}
li = cores['limpar']
vm = cores['vermelho']
am = cores['amarelo']

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
tot = (dias * 60) + (km * 0.15)
print('{}O total a pagar é de {}{}R${:.2f}{}'.format(vm, li, am, tot, li))

# Solução Gustavo Guanabara (CursoemVideo)
# dias = int(input('Quantos dias alugados? '))
# km = float(input('Quantos Km rodados? '))
# pago = (dias * 60) + (km * 0.15)
# print('O total a pagar é de R${:.2f}'.format(pago))
