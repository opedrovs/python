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

# Utilizando o Do. While
totmais18 = tothomem = totmulher20 = 0
print(f'{"FIM DO PROGRAMA":=^31}')
while True:
    print(f'{am}-{li}' * 27)
    print(f'{az}{f"CADASTRE UMA PESSOA":^28}{li}')
    print(f'{am}-{li}'*27)
    idade = int(input('Idade: '))
    sexo = str(input(f'Sexo: [{az}M{li}/{rx}F{li}] ')).upper().strip()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input(f'Sexo: [{az}M{li}/{rx}F{li}] ')).upper().strip()[0]
    print(f'{am}-{li}' * 27)
    resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).upper().strip()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).upper().strip()[0]
    if idade > 18:
        totmais18 += 1
    if sexo in 'Mm':
        tothomem += 1
    elif sexo in 'Ff':
        if idade < 20:
            totmulher20 += 1
    if resp == 'N':
        break
print(f'{am}{f" {az}FIM DO PROGRAMA{am} ":=^43}{li}')
print(f'Total de pessoas com mais de 18 anos: {vd}{totmais18}{li}')
if tothomem > 1:
    print(f'Ao todo temos {am}{tothomem}{li} homens cadastrados')
else:
    print(f'Ao todo temos {am}{tothomem}{li} homem cadastrado')
if totmulher20 > 1:
    print(f'E temos {vm}{totmulher20}{li} mulheres com menos de 20 anos')
else:
    print(f'E temos {vm}{totmulher20}{li} mulher com menos de 20 anos')

# Minha solução
'''
totmais18 = tothomem = totmulher20 = 0
print(f'{"FIM DO PROGRAMA":=^31}')
resp = 'S'
while resp != 'N':
    print('-'*27)
    print(f'{"CADASTRE UMA PESSOA":^28}')
    print('-'*27)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-'*27)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if idade > 18:
        totmais18 += 1
    if sexo == 'M':
        tothomem += 1
    elif sexo == 'F':
        if idade < 20:
            totmulher20 += 1
print(f'{" FIM DO PROGRAMA ":=^31}')
print(f'Total de pessoas com mais de 18 anos: {totmais18}')
print(f'Ao todo temos {tothomem} homens cadastrados')
print(f'E temos {totmulher20} mulheres com menos de 20 anos')
'''
