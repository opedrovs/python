# Minha solução
cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'vermelho': '\033[0;31m',
    'amarelo': '\033[0;33m'
}
li = cores['limpar']
vd = cores['verde']
vm = cores['vermelho']
am = cores['amarelo']

vel = float(input('Qual é a velocidade atual do carro? '))
# Calculo de multa
if vel > 80:
    print('{}MULTADO! Você excedeu o limite permitido que é de 80Km/h'.format(vm))
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de {}R${:.2f}!{}'.format(am, multa, li))
print('{}Tenha um bom dia! Dirija com segurança!{}'.format(vd, li))

# Solução Gustavo Guanabara
'''
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
'''
