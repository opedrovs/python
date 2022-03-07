dis = float(input('Qual é a distância da sua viagem? '))
if dis > 200:
    preco = dis * 0.45
else:
    preco = dis * 0.50
print('Você está prestes a começar uma viagem de {}Km.'.format(dis))
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
