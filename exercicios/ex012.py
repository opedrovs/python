# Minha solução
produ = input('O produto que deseja comprar: ')
preco = float(input('Preço atual do produto, R$'))
porcen = (preco / 100) * 5
descon = preco - porcen
print('O produto {} custava R${:.2f}, mas agora está com uma promoção de 5%'.format(produ, preco), end='')
print(', custando cerca de R${:.2f}.'.format(descon))

# Solução Gustavo Guanabara (CursoemVideo)
# preço = float(input('Qual é o preço do produto? R$'))
# novo = preço - (preço * 5 / 100)
# print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
