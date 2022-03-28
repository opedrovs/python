from datetime import date

cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
rx = cores['roxo']

# Minha solução
anoatual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = anoatual - nasc
print(f'Quem nasceu em {am}{nasc}{li} tem {am}{idade} anos {li}em {rx}{anoatual}{li}.')
if idade < 18:
    print(f'Ainda faltam {vd}{18-idade} anos {li}para o alistamento')
    print(f'Seu alistamento será em {vm}{anoatual+(18-idade)}{li}.')
elif idade == 18:
    print(f'Você tem que se alistar {vm}IMEDIATAMENTE!{li}')
else:
    print(f'Você já deveria ter se alistado há {vm}{idade-18} anos{li}.')
    print(f'Seu alistamento foi em {vd}{anoatual-(idade-18)}{li}.')

# Solução Gustavo Guanabara
'''
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = saldo + atual
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
'''
