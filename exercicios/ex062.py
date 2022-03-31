cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']
rx = cores['roxo']

# Minha solução
'''
print('Gerador de PA')
print('-=' * 12)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
cont = 1
tottermo = 0
while cont != 0:
    print(f'{am}{pri}{li}', end=' → ')
    pri += raz
    cont += 1
    tottermo += 1
    if cont > 10:
        print(f'{az}PAUSA{li}')
        mais = int(input(f'Quantos termos você quer mostrar a mais? '))
        if mais == 0:
            cont = 0
        else:
            print(f'{am}{pri}{li}', end=' → ')
            cont -= mais - 1
            pri += raz
            tottermo += 1
print(f'Progressão finalizada com {vd}{tottermo}{li} termos mostrados.')
'''

# Minha solução feito através da correção do ex061
print('Gerador de PA')
print('-=' * 12)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
termo = pri
cont = 1
mais = 1
tottermos = 0
while cont <= 10 and mais != 0:
    print(f'{termo} → ', end='')
    termo += raz
    cont += 1
    tottermos += 1
    if cont > 10:
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostrar a mais? '))
        if mais != 0:
            cont -= mais
print(f'Progressão finalizada com {tottermos} termos mostrados.')

# Solução Gustavo Guanabara
'''
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progresso finalizada com {} termos mostrados.'.format(total))
'''
