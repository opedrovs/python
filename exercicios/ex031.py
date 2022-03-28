# Minha solução
cores = {
    'limpa': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}
dis = float(input('Qual é a distância da sua viagem? '))
if dis >= 200:
    preco = dis * 0.45
else:
    preco = dis * 0.50
print('{}Você está prestes a começar uma viagem de {}Km.'.format(cores['verde'], dis))
print('E o preço da sua passagem será de {}R${:.2f}'.format(cores['amarelo'], preco))

# Solução Gustavo Guanabara
'''
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
'''
# OU
'''
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
'''
