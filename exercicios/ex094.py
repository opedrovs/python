# Minha solução
cadastro = {}
lista = []
soma = media = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while cadastro['sexo'] != 'M' and cadastro['sexo'] != 'F':
        print('ERRO! Por favor, digite apenas M ou F.')
        cadastro['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    lista.append(cadastro.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resp != 'S' and resp != 'N':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for pessoas in lista:
    if pessoas['sexo'] == 'F':
        print(f'{pessoas["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for pessoas in lista:
    if pessoas['idade'] > media:
        for chave, pessoa in pessoas.items():
            print(f'{chave} = {pessoa}; ', end='')
        print()
print('<< ENCERRADO >>')
