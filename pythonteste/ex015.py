# Laço de repetição "tipo" Do... While

# Com teste lógico, caso o número seja: 999
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma é {s}')

#
'''
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print(f'A soma é {s}')
'''
