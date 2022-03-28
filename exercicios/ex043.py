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
peso = float(input('Qual é seu peso? (Kg) '))
alt = float(input('Qual é sua altura? (m) '))
imc = (peso / (alt ** 2))
print(f'O {am}IMC{li} dessa pessoa é de {am}{imc:.1f}{li}')
if imc < 18.5:
    # ABAIXO do peso
    print(f'Você está {vm}ABAIXO{li} do peso normal')
elif imc < 25:
    # Peso NORMAL
    print(f'Você está na faixa de {vd}PESO NORMAL{li}')
elif imc < 30:
    # SOBREPESO
    print(f'Você está em {az}SOBREPESO{li}')
elif imc < 40:
    # OBESIDADE
    print(f'Você está em {vm}OBESIDADE!{li}')
else:
    # OBESIDADE MÓRBIDA
    print(f'Você está em {vm}OBESIDADE MÓRBIDA, cuidado!{li}')

# Solução Gustavo Guanabara
'''
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
'''
