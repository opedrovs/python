from datetime import date
# Minha solução
cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}
l = cores['limpar']
vd = cores['verde']
am = cores['amarelo']

anoatual = date.today().year
ano = int(input('Ano de Nascimento: ').strip())
idade = anoatual - ano
print(f'O atleta tem {vd}{idade} anos{l}.')
if idade <= 9:
    classif = 'MIRIM'
elif idade <= 14:
    classif = 'INFANTIL'
elif idade <= 19:
    classif = 'JÚNIOR'
elif idade <= 25:
    classif = 'SÊNIOR'
else:
    classif = 'MASTER'
print(f'Classificação: {am}{classif}{l}')

# Solução Gustavo Guanabara
'''
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
'''
