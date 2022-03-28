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
print('Gerador de PA')
print('-='*12)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
ini = 1
tottermo = 0
while ini != 0:
    print(f'{am}{pri}{li}', end=' > ')
    pri += raz
    ini += 1
    tottermo += 1
    if ini > 10:
        print(f'{az}PAUSA{li}')
        mais = int(input(f'Quantos termos você quer mostrar a mais? '))
        if mais == 0:
            ini = 0
        else:
            print(f'{am}{pri}{li}', end=' > ')
            ini -= mais - 1
            pri += raz
            tottermo += 1
print(f'Progressão finalizada com {vd}{tottermo}{li} termos mostrados.')
