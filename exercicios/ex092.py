from datetime import date
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
        cadastro['salário'] = float(input('Salário: R$'))
        cadastro['aposentadoria'] = (cadastro['contratação'] - nasc) + 35
        break
print('-=' * 30)
for chave, valor in cadastro.items():
    print(f'  - {chave} tem o valor {valor}')
