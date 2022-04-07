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
print(f'A soma dos {rx}{valores}{li} valores foi {vd}{soma}{li}!')

# Solução Gustavo Guanabara
'''
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')
'''
