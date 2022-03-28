# AINDA FAZENDO
print('-'*28)
print('Sequência de Fibonacci')
print('-'*28)
termo = int(input('Quantos termos você quer mostrar? '))
print('='*28)
cont = 0
calc = 0
i = 0
i2 = 1
soma = 0
while cont < termo:
    soma += i + i2
    print(f'{soma}', end=' → ')
    i += 1
    i2 += 1
    cont += 1
print('FIM')
print('='*28)
