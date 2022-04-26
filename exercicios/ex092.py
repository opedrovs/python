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

atual = date.today().year
cadastro = {}
while True:
    cadastro['nome'] = str(input('Nome: '))
    nasc = int(input('Ano de Nascimento: '))
    cadastro['idade'] = atual - nasc
    cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if cadastro['ctps'] == 0:
        break
    else:
        cadastro['contratação'] = int(input('Ano de Contratação: '))
        cadastro['salário'] = float(input(f'Salário: {vd}R${li}'))
        cadastro['aposentadoria'] = (cadastro['contratação'] - nasc) + 35
        break
print('-=' * 30)
for chave, valor in cadastro.items():
    print(f'  - {az}{chave}{li} tem o valor {am}{valor}{li}')
