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
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).strip().upper()
    if resp == 'N':
        break
valores.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {az}{len(valores)}{li} elementos.')
print(f'Os valores em ordem decrescente são {am}{valores}{li}')
if 5 in valores:
    print(f'O valor 5 {vd}faz parte{li} da lista!')
else:
    print(f'O valor 5 {vm}não foi encontrado{li} na lista!')
