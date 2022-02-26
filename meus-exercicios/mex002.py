prod = input('Nome do produto que deseja comprar: ')
preco = float(input('Preço do {} que está comprando. R$'.format(prod)))
entreg = float(input('O dinheiro que entregou para comprar o {}. R$'.format(prod)))
troco = entreg - preco
print('-' * 56)
print('Você comprou o {} que custava cerca de R${:.2f}.'.format(prod, preco))
print('Deu R${:.2f} em dinheiro e irá receber R${:.2f} de troco. \nVolte Sempre!'.format(entreg, troco))
print('-' * 56)
