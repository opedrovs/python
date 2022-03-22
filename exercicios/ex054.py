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

from datetime import date
# Minha solução
atual = date.today().year
maior = 0
menor = 0
for cont in range(1, 8):
    nasc = int(input(f'{az}Em que ano a {am}{cont}º{az} pessoa nasceu?{l} '))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {am}{maior}{vd} pessoas maiores{l} de idade')
print(f'E também tivemos {am}{menor}{vm} pessoas menores{l} de idade')
