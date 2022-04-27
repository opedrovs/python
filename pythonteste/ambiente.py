'''def lin():
    print('-' * 30)


# Programa Principal
lin()
print('     CURSO EM VÍDEO')
lin()
print('     APRENDA PYTHON')
lin()
print('     GUSTAVO GUANABARA')
lin()'''

# Usando def com parâmetros (rotina)

'''
def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


# Programa Principal
título('    CURSO EM VÍDEO   ')
título(' PYTHON É MUITO BOM! ')
título('Oi')
'''

# Somando valores (limitado a 2 valores)


'''def soma(a=0, b=0): # a/b recebe 0 caso não tenha um valor
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Principal
soma(b=4, a=5)
soma(8, 9)
soma(2, 1)
soma(4, 1)
soma(3)

# Sem Função
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)'''

# Empacotar parâmetros (Aceitar vários valores aleatórios)


'''def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')
    #for valor in núm:
    #    print(f'{valor} ', end='')
    #print('FIM!')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''


# Soma do Empacotamento


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)

# Usando listas em Função


'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)'''
