# Minha solução
print('Gerador de PA')
print('-='*12)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
ini = 1
tottermo = 0
while ini <= 10 and ini != 0:
    print(f'{pri}', end=' > ')
    pri += raz
    ini += 1
    tottermo += 1
    if ini > 10:
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostrar a mais? '))
        if mais == 0:
            ini = 0
        else:
            print(f'{pri}', end=' → ')
            ini -= mais - 1
            pri += raz
            tottermo += 1
print(f'Progressão finalizada com {tottermo} termos mostrados.')
