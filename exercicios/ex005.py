# Minha segunda solução
cores = {
    'limpar': '\033[m',
    'vermel': '\033[0;31m',
    'amarel': '\033[0;33m',
    'azul': '\033[0;34m'
}
num = int(input('Digite um número: '))
suc = num+1
ant = num-1
print('O sucessor de {}{}{} é {}{}{}.'.format(cores['azul'], num, cores['limpar'], cores['amarel'], suc, cores['limpar']))
print('O antecessor de {}{}{} é {}{}{}.'.format(cores['azul'], num, cores['limpar'], cores['vermel'], ant, cores['limpar']))

# Minha segunda solução
# print('O sucessor de {} é {}.'.format(num, num+1))
# print('O antecessor de {} é {}.'.format(num, num-1))



# Solução Gustavo Guanabara (CursoemVideo)
# n = int(input('Digite um número: '))
# a = n-1
# s = n+1
# print('Analisando o número {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))

# Ou

# print('Analisando o número {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
