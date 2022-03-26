# Minha solução
print('Gerador de PA')
print('-='*12)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
ini = 1
while ini <= 10:
    if raz == 0:
        print('Razão inválida. Tente novamente!')
        ini += 10
    else:
        print(f'{pri}', end=' → ')
        pri += raz
        ini += 1
print('FIM')
