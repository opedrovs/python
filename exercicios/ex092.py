from datetime import date

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
atual = date.today().year
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cadastro['idade'] = atual - nasc
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input(f'Salário: {vd}R${li}'))
    cadastro['aposentadoria'] = (cadastro['contratação'] - nasc) + 35
print('-=' * 30)
for chave, valor in cadastro.items():
    print(f'  - {az}{chave}{li} tem o valor {am}{valor}{li}')

# Solução Gustavo Guanabara
'''from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')'''
