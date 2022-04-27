cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']
rx = cores['roxo']

# Minha solução
cadastro = {}
lista = []
soma = media = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input(f'Sexo: [{az}M{li}/{rx}F{li}] ')).strip().upper()
    while cadastro['sexo'] != 'M' and cadastro['sexo'] != 'F':
        print(f'{vm}ERRO!{li} Por favor, digite apenas {az}M{li} ou {rx}F{li}.')
        cadastro['sexo'] = str(input(f'Sexo: [{az}M{li}/{rx}F{li}] ')).strip().upper()
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    lista.append(cadastro.copy())
    resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).strip().upper()
    while resp != 'S' and resp != 'N':
        print(f'{vm}ERRO!{li} Responda apenas {vd}S{li} ou {vm}N{li}.')
        resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {vd}{len(lista)}{li} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A média de idade é de {am}{media:.2f}{li} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for pessoas in lista:
    if pessoas['sexo'] == 'F':
        print(f'{az}{pessoas["nome"]}{li} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for pessoas in lista:
    if pessoas['idade'] > media:
        for chave, pessoa in pessoas.items():
            print(f'{az}{chave}{li} = {am}{pessoa}{li}; ', end='')
        print()
print(f'{am}<< {az}ENCERRADO {am}>>{li}')

# Solução Gustavo Guanabara
'''galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')'''
