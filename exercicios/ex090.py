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
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['média'] = float(input(f'Média de {cadastro["nome"]}: '))
if cadastro['média'] >= 7:
    cadastro['situação'] = f'{vd}Aprovado{li}'
elif cadastro['média'] >= 5:
    cadastro['situação'] = f'{am}Recuperação{li}'
else:
    cadastro['situação'] = f'{vm}Reprovado{li}'
print('-=' * 30)
for chave, aluno in cadastro.items():
    print(f'  - {chave} é igual a {az}{aluno}{li}')

# Solução Gustavo Guanabara
'''
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
'''
