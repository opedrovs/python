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
        sacar %= 1
    break
print(f'{az}={li}'*30)
print(f'{rx}Volte sempre ao BANCO CEV! Tenha um bom dia!{li}')
