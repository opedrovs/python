num = [2, 5, 9, 1]
num[2] = 3 # Trocar um valor
num.append(7) # Adicionar um valor no final
# num.sort() # Alinhar do maior para o menor (ex: 1, 2, 3, 4...)
num.sort(reverse=True) # Alinhar do menor para o maior (ex: 5, 4, 3, 2...)
num.insert(2, 2) # Adicionar o valor 2 na posição 2
# num.pop() # Remover o último valor da lista
# num.pop(2) # Remover o valor da posição 2
# num.remove(1) # Remover o valor 1
if 5 in num: # SE tiver o valor 5 em num, então remove-lo
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista em {len(num)} elementos')

# Formatar

'''
valores = [] # OU: valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
'''

# Pecularidade do Python
'''
a = [2, 3, 4, 7]
b = a[:] # Passando apenas os valores de A, sem ligação, apenas uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Cópia com ligação:
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''
