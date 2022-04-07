'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são IMUTÁVEIS
# lanche[1] = 'Refrigerante'

for comida in lanche:
    print(f'Eu vou comer {comida} ')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

print(sorted(lanche))
print(lanche)
'''

# Outro exemplo:
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
# print(len(c))
# print(c.count(5)) # Quantos 5 tem na váriavel composta c
# print(c.index(8)) # Mostra em qual posição está o 8
print(c.index(5, 1)) # Você quer ver quantos 5 tem apartir da posição 1 (a posição 0 tem o 5, ele pula e começa do 1)
'''

# Exemplo de Dados de tipos diferentes:
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # APAGAR a memória (Apagar uma variável)
print(pessoa)

