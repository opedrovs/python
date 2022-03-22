cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
l = cores['limpar']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']
rx = cores['roxo']

# Minha solução
valores = 0
soma = 0
for cont in range(1, 7):
    num = int(input(f'{rx}Digite o {am}{cont}º{rx} valor:{l} '))
    if num % 2 == 0:
        valores += 1
        soma += num
print(f'A soma dos {vd}{valores}{l} valores PARES é de {vd}{soma}{l}.')
