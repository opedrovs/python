cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',

}

# Minha solução (Jeito ERRADO pois só reconhece 4 algarismos!)
'''
num = str(input('Informe um número: '))
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))
'''

# Solução Gustavo Guanabara
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}{}{}'.format(cores['amarelo'], u, cores['limpar']))
print('Dezena: {}{}{}'.format(cores['amarelo'], d, cores['limpar']))
print('Centena: {}{}{}'.format(cores['amarelo'], c, cores['limpar']))
print('Milhar: {}{}{}'.format(cores['amarelo'], m, cores['limpar']))
