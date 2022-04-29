# Métodos de Help

# 1. Clicando no "Python Console", digitar "help()" e colocar o comando que quer ver, e "quit" para sair.

# 2. Utilizando o help()
# help(input)

# 3. Utilizando o __doc__, o atributo do input
# print(input.__doc__)

# Docstrings, criar sua própria


'''def contador(i, f, p):
    """
        -> Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
        Função criada por Gustavo Guananabara do canal CursoemVídeo.
        """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)'''

# Parâmetros opcionais


'''def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Gustavo Guanabara para o CursoemVídeo.
    """
    s = a + b + c
    print(f'A soma vale {s}')


# soma(3, 2)
soma(c=3, b=2)'''

# Sobre escopos


'''def teste():
    x = 8 # escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2 # escopo global
print(f'No programa principal, n vale {n}')
teste()
# print(f'Na função teste, x vale {x}'), então por isso dá erro'''


'''def teste(b):
    a = 8 # A local
    b += 4 # B local
    c = 2 # C local
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5 # A global
teste(a)
print('-' * 15)
print(f'A fora vale {a}')'''

# Tratar o A de forma global (dentro da função)


'''def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print('-' * 15)
print(f'A fora vale {a}')'''


'''def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')'''

# Retornando valores
# Funções que retornam resultado são úteis para personalização dos resultados


'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s # retornar o valor de s para dentro da variável de resposta(r1, r2, r3...)


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Meus cálculos deram {r1}, {r2} e {r3}.')'''

# Parte prática
# Calcular Fatorial


'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}')'''

# Se o valor é par
# O return não é apenas para número, também serve para valores lógicos, inteiros, literais, listas, tuplas, ...


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
