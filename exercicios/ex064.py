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
num = 0
soma = 0
totnum = 0
while num != 999:
    num = int(input(f'{az}Digite um número {am}[999 para parar]{li}: '))
    if num != 999:
        soma += num
        totnum += 1
if totnum == 1:
    print(f'Você digitou {rx}{totnum}{li} número e a soma entre ele foi {vd}{soma}{li}.')
else:
    print(f'Você digitou {rx}{totnum}{li} números e a soma entre eles foi {vd}{soma}{li}.')

# Solução Gustavo Guanabara
'''
núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    cont += 1
    soma += núm
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
'''
