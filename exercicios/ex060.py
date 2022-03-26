# Minha solução
num = int(input('Digite um número para \ncalcular seu Fatorial: '))
fat = 1
ordem = 2
print(f'Calculando {num}! =', end=' ')
while num >= ordem:
    print(f'{num}', end=' x ')
    fat *= num
    num -= 1
print(f'1 = {fat}')
