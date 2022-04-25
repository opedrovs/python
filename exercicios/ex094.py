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
    media += soma / len(lista)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resp != 'S' and resp != 'N':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for pessoa in lista:
    print(pessoa)
