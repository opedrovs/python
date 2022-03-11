# Minha solução

cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}

l = cores['limpar']
am = cores['amarelo']
az = cores['azul']

num = int(input('Digite um número: '))
print('{}={}'.format(az, l) * 11)
print('{} x {:2} = {}{}{}'.format(num, 1, am, num*1, l))
print('{} x {:2} = {}{}{}'.format(num, 2, am, num*2, l))
print('{} x {:2} = {}{}{}'.format(num, 3, am, num*3, l))
print('{} x {:2} = {}{}{}'.format(num, 4, am, num*4, l))
print('{} x {:2} = {}{}{}'.format(num, 5, am, num*5, l))
print('{} x {:2} = {}{}{}'.format(num, 6, am, num*6, l))
print('{} x {:2} = {}{}{}'.format(num, 7, am, num*7, l))
print('{} x {:2} = {}{}{}'.format(num, 8, am, num*8, l))
print('{} x {:2} = {}{}{}'.format(num, 9, am, num*9, l))
print('{} x {:2} = {}{}{}'.format(num, 10, am, num*1, l))
print('{}={}'.format(az, l) * 11)

# Minha segunda solução

# nx1 = num * 1
# nx2 = num * 2
# nx3 = num * 3
# nx4 = num * 4
# nx5 = num * 5
# nx6 = num * 6
# nx7 = num * 7
# nx8 = num * 8
# nx9 = num * 9
# nx10 = num*10
# print('=' * 11)
# print('{} x 1 =  {}'.format(num, nx1))
# print('{} x 2 =  {}'.format(num, nx2))
# print('{} x 3 =  {}'.format(num, nx3))
# print('{} x 4 =  {}'.format(num, nx4))
# print('{} x 5 =  {}'.format(num, nx5))
# print('{} x 6 =  {}'.format(num, nx6))
# print('{} x 7 =  {}'.format(num, nx7))
# print('{} x 8 =  {}'.format(num, nx8))
# print('{} x 9 =  {}'.format(num, nx9))
# print('{} x 10 = {}'.format(num, nx10))
# print('=' * 11)

# Solução Gustavo Guanabara (CursoemVideo)

# num = int(input('Digite um número para ver sua tabuada: '))
# print('-' * 12)
# print('{} x {:2} = {}'.format(num, 1, num*1))
# print('{} x {:2} = {}'.format(num, 2, num*2))
# print('{} x {:2} = {}'.format(num, 3, num*3))
# print('{} x {:2} = {}'.format(num, 4, num*4))
# print('{} x {:2} = {}'.format(num, 5, num*5))
# print('{} x {:2} = {}'.format(num, 6, num*6))
# print('{} x {:2} = {}'.format(num, 7, num*7))
# print('{} x {:2} = {}'.format(num, 8, num*8))
# print('{} x {:2} = {}'.format(num, 9, num*9))
# print('{} x {} = {}'.format(num, 10, num*10))
# print('-' * 12)
