'''
num = int(input('Digite um número para ver sua tabuada: '))
for cont in range(1, 11):
    print(f'{num} x {cont:2} = {num*cont}')
'''

# OU (colocando o limite do final)


num = int(input('Digite um número para ver sua tabuada: '))
fim = int(input('Digite até o número que quer ter essa tabuada: '))

for cont in range(1, fim+1):
    print(f'{num} x {cont:2} = {num*cont}')
