from datetime import date

cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
az = cores['azul']
rx = cores['roxo']

# Minha solução SIMPLIFICADO (após ver resposta)
ano = int(input('Que ano quer analisar? Coloque {}0{} para analisar o ano atual: '.format(rx, li)))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}O ano {}{}{} é BISSEXTO{}'.format(vd, az, ano, vd, li))
else:
    print('{}O ano {}{}{} NÃO é BISSEXTO{}'.format(vm, az, ano, vm, li))

# Minha solução
'''
cores = {
    'limpa': '\033[m',
    'roxo': '\033[0;35m',
    'azul': '\033[0;34m',
    'verde': '\033[0;32m',
    'vermel': '\033[0;31m'
}
ano = int(input('Que ano quer analisar? Coloque {}0{} para analisar o ano atual: '.format(cores['roxo'], cores['limpa'])))
anoatual = int(datetime.today().strftime('%Y'))

if ano == 0:
    if anoatual % 4 == 0 and anoatual % 100 != 0 or anoatual % 400 == 0:
        print('{}O ano {}{}{} é BISSEXTO{}'.format(cores['verde'], cores['azul'], anoatual, cores['verde'], cores['limpa']))
    else:
        print('{}O ano {}{}{} NÃO é BISSEXTO{}'.format(cores['vermel'], cores['azul'], anoatual, cores['vermel'], cores['limpa']))
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}O ano {}{}{} é BISSEXTO{}'.format(cores['verde'], cores['azul'], ano, cores['verde'], cores['limpa']))
else:
    print('{}O ano {}{}{} NÃO é BISSEXTO{}'.format(cores['vermel'], cores['azul'], ano, cores['vermel'], cores['limpa']))
'''

# Solução Gustavo Guanabara
'''
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
'''
