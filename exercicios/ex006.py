# Minha solução

cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarel': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
# Variáveis com as Cores
lim = cores['limpar']
roxo = cores['roxo']
verd = cores['verde']
ama = cores['amarel']
az = cores['azul']

num = int(input('Digite um número: '))
dob = num * 2
tri = num * 3
raiz = num ** (1/2)
print('O dobro de {}{}{} é {}{}{}, o triplo é {}{}{}. e a raiz quadrado é {}{:.2f}{}.'.format(az, num, lim, verd, dob, lim, ama, tri, lim, roxo, raiz, lim))

# Solução Gustavo Guanabara (CursoemVideo)
# n = int(input('Digite um número: '))
# d = n * 2
# t = n * 3
# r = n ** (1/2)
# print('O dobro de {} vale {}.'.format(n, d))
# print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
