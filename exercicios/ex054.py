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
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for cont in range(1, 8):
    nasc = int(input(f'{az}Em que ano a {am}{cont}º{az} pessoa nasceu?{li} '))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {am}{maior}{li} pessoas {vd}maiores{li} de idade')
print(f'E também tivemos {am}{menor}{li} pessoas {vm}menores{li} de idade')

# Solução Gustavo Guanabara
'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
'''
