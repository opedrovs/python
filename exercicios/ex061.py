cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vm = cores['vermelho']
am = cores['amarelo']
az = cores['azul']
rx = cores['roxo']

# Minha solução
print('Gerador de PA')
print('-='*12)
pri = int(input(f'{rx}Primeiro termo:{li} '))
raz = int(input(f'{rx}Razão da PA:{li} '))
ini = 1
while ini <= 10:
    if raz == 0:
        print(f'{vm}Razão inválida. Tente novamente!{li}')
        ini += 10
    else:
        print(f'{am}{pri}{li}', end=' → ')
        pri += raz
        ini += 1
print(f'{vm}FIM{li}')
