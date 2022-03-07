# Minha solução
from datetime import datetime
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
anoatual = int(datetime.today().strftime('%Y'))

if ano == 0:
    if (anoatual % 4 == 0 and anoatual % 100 != 0) or (anoatual % 400 == 0):
        print('O ano {} é BISSEXTO'.format(anoatual))
    else:
        print('O ano {} NÃO é BISSEXTO'.format(anoatual))
elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))
