cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
l = cores['limpar']
am = cores['amarelo']
rx = cores['roxo']

# Minha solução após ver a resposta:
soma = 0
valores = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        soma += cont
        valores += 1
print(f'A soma de todos os {rx}{valores}{l} valores solicitados é {am}{soma}{l}')

# Minha solução

'''
valores = 0
soma = 0
for cont in range(1, 501):
    if cont % 3 == 0 and cont % 2 != 0:
        valores += 1
        soma += cont
print(f'A soma de todos os {rx}{valores}{l} valores solicitados é {am}{soma}{l}')
'''

# Solução Gustavo Guanabara:
'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
'''
