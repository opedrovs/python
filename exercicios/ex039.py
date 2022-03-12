from datetime import date
# Minha solução
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
l = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
rx = cores['roxo']

ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print(f'Quem nasceu em {am}{ano}{l} tem {am}{idade} anos {l}em {rx}{anoatual}{l}.')

if idade <= 18:
    print(f'Ainda faltam {vd}{18-idade} anos {l}para o alistamento')
    print(f'Seu alistamento será em {vm2}{anoatual+(18-idade)}{l}.')
else:
    print(f'Você já deveria ter se alistado há {vm}{idade-18} anos{l}.')
    print(f'Seu alistamento foi em {vd}{anoatual-(idade-18)}{l}.')
