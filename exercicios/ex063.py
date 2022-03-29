# Solução feita com ajuda dos comentários:
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
