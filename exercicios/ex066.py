cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']
rx = cores['roxo']

# Minha solução
valores = soma = 0
while True:
    num = int(input(f'{az}Digite um valor {am}(999 para parar){li}: '))
    if num == 999:
        break
    valores += 1
    soma += num
if valores > 1:
    print(f'A soma dos {rx}{valores}{li} valores foi {vd}{soma}{li}!')
else:
    print(f'A soma de {rx}{valores}{li} valor foi {vd}{soma}{li}!')
