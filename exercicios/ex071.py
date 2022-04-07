cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

# Minha solução
print(f'{az}='*30)
print(f'{am}{"BANCO CEV":^30}')
print(f'{az}={li}'*30)
sacar = int(input(f'Que valor você quer sacar? {vd}R${li}'))
# Cédulas: R$50, R$20, R$10, R$1
cedula50 = cedula20 = cedula10 = cedula1 = 0
while True:
    if sacar // 50:
        cedula50 = sacar // 50
        print(f'Total de {vd}{cedula50}{li} cédulas de R$50')
        sacar %= 50
    if sacar // 20:
        cedula20 = (sacar % 50) // 20
        print(f'Total de {vd}{cedula20}{li} cédulas de R$20')
        sacar %= 20
    if sacar // 10:
        cedula10 = ((sacar % 50) % 20) // 10
        print(f'Total de {vd}{cedula10}{li} cédulas de R$10')
        sacar %= 10
    if sacar // 1:
        cedula1 = (((sacar % 50) % 20) % 10) // 1
        print(f'Total de {vd}{cedula1}{li} cédulas de R$1')
    break
print(f'{az}={li}'*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

# Solução Gustavo Guanabara
'''
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
'''
