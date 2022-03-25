'''
for c in range(1, 5):
    num = int(input('Digite um valor: '))
print('FIM')
'''
#
'''
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')
'''
##
'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('FIM')
'''
##

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares')
