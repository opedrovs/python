# Minha solução
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
l = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

peso = float(input('Qual é seu peso? (Kg) '))
alt = float(input('Qual é sua altura? (m) '))
imc = (peso / (alt * alt))
print(f'O {am}IMC{l} dessa pessoa é de {am}{imc:.1f}{l}')
if imc <= 18.5:
    # ABAIXO do peso
    print(f'Você está {vm}ABAIXO{l} do peso normal')
elif imc <= 25:
    # Peso NORMAL
    print(f'Você está na faixa de {vd}PESO NORMAL{l}')
elif imc <= 30:
    # SOBREPESO
    print(f'Você está em {az}SOBREPESO{l}')
elif imc <= 40:
    # OBESIDADE
    print(f'Você está em {vm}OBESIDADE!{l}')
else:
    # OBESIDADE MÓRBIDA
    print(f'Você está em {vm}OBESIDADE MÓRBIDA, cuidado!{l}')
