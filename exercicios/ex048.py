cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
l = cores['limpar']
am = cores['amarelo']
rx = cores['roxo']

valores = 0
soma = 0
for cont in range(0, 501):
    if cont % 2 != 0 and cont % 3 == 0:
        valores += 1
        soma += cont

print(f'A soma de todos os {rx}{valores}{l} valores solicitados é {am}{soma}{l}')

