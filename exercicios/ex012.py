produ = input('O produto que deseja comprar: ')
preco = float(input('Preço atual do produto, R$'))
promo = (preco / 100) * 5
descon = preco - promo

print('O produto {} custava R$ {:.2f}, mas agora está com uma promoção de 5%, custando cerca de R$ {:.2f}.'.format(produ, preco, descon))
