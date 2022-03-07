# Minha solução
cores = {
    'limpa': '\033[m',
    'verde': '\033[0;32m',
    'vermel': '\033[0;31m',
    'amarelo': '\033[0;33m'
}
vel = float(input('Qual é a velocidade atual do carro? '))
# Calculo de multa
if vel > 80:
    print('{}MULTADO! Você excedeu o limite permitido que é de 80Km/h'.format(cores['vermel']))
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de {}R${:.2f}!{}'.format(cores['amarelo'], multa, cores['limpa']))

print('{}Tenha um bom dia! Dirija com segurança!{}'.format(cores['verde'], cores['limpa']))

# Solução Gustavo Guanabara
'''
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
'''
