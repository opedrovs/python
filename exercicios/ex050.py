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
valores = 0
soma = 0
for cont in range(1, 7):
    num = int(input(f'{rx}Digite o {am}{cont}º{rx} valor:{li} '))
    if num % 2 == 0:
        valores += 1
        soma += num
if valores == 1:
    print(f'A soma de {am}{valores}{li} valor {az}PAR{li} informado é de {vd}{soma}{li}.')
else:
    print(f'A soma dos {am}{valores}{li} valores {az}PARES{li} informados é de {vd}{soma}{li}.')

# Solução Gustavo Guanabara:
'''
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
'''
