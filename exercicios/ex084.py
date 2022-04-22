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
pessoas = []
dado = []
maior = menor = cont = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    resp = ' '
    while resp != 'S' and resp != 'N':
        resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {am}{len(pessoas)}{li} pessoas.')
for peso in pessoas:
    if cont == 0:
        maior = menor = peso[1]
    else:
        if peso[1] > maior:
            maior = peso[1]
        if peso[1] < menor:
            menor = peso[1]
    cont += 1
print(f'O maior peso foi de {vd}{maior}Kg{li}. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'{az}[{pessoa[0]}]{li} ', end='')
print()
print(f'O menor peso foi de {vm}{menor}Kg{li}. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'{az}[{pessoa[0]}]{li} ', end='')
print()


# Solução Gustavo Guanabara
'''
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
'''
