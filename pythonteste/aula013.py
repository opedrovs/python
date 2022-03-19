'''
for c in range(0, 6):
    print(c)
print('FIM')

#

for c in range(6, 0, -1):
    print(c)
print('FIM')

#

for c in range(0, 7, 2):
    print(c)
print('FIM')

#

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)

#

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if inicio < fim:
    for c in range(inicio, fim+1, passo):
        print(c)
else:
    for c in range(inicio, fim-1, -passo):
        print(c)
print('FIM')
'''

#
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')
