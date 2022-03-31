# Minha solução após ver resposta:
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
termo = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} → {t2} → ', end='')
cont = 3
while cont <= termo:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('~'*30)

# Solução feita com ajuda dos comentários:
'''
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
termo = int(input('Quantos termos você quer mostrar? '))
print('~'*30)
cont = 1
anterior = 0
proxima = 1
soma = 1
while cont <= termo:
    print(anterior, end=' → ')
    cont += 1
    soma = proxima + anterior
    anterior = proxima
    proxima = soma
print('FIM')
print('~'*30)
'''

# Solução Gustavo Guanabara
'''
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('~'*30)
'''
