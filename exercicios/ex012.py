cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

# Minha solução
produ = input('O produto que deseja comprar: ')
preco = float(input('Preço atual do produto, R$'))
porcen = (preco / 100) * 5
descon = preco - porcen
print(f'O produto {az}{produ}{li} custava {vm}R${preco:.2f}{li}, mas agora está com uma promoção de {am}5%{li}', end='')
print(f', custando cerca de {vd}R${descon:.2f}{li}.')
# print('O produto {} custava R${:.2f}, mas agora está com uma promoção de 5%'.format(produ, preco), end='')
# print(', custando cerca de R${:.2f}.'.format(descon))

# Solução Gustavo Guanabara (CursoemVideo)
# preço = float(input('Qual é o preço do produto? R$'))
# novo = preço - (preço * 5 / 100)
# print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
