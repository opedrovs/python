# Minha solução:
num = int(input('Digite um número para ver sua tabuada: '))
for cont in range(1, 11):
    print(f'{num} x {cont:2} = {num*cont}')

# Outra solução, onde coloca limite de final:
'''
num = int(input('Digite um número para ver sua tabuada: '))
fim = int(input('Até que linha quer ter na tabuada: '))

for cont in range(1, fim + 1):
    print(f'{num} x {cont:2} = {num * cont}')
'''
