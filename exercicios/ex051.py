# AINDA FAZENDO
print('='*28)
print('{:^28}'.format('10 TERMOS DE UMA PA'))
print('='*28)

pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for cont in range(pri, 10, razao):
    print(cont, end=' → ')
print('ACABOU')
