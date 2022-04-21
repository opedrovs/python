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
for p in pessoas:
    if cont == 0:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        if p[1] < menor:
            menor = p[1]
    cont += 1
print(f'O maior peso foi de {vd}{maior}Kg{li}. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{az}{p[0]}{li} ', end='')
print(f'\nO menor peso foi de {vm}{menor}Kg{li}. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{az}{p[0]}{li} ', end='')
