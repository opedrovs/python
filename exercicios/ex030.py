# Minha solução
cores = {
    'limpar': '\033[m',
    'roxo': '\033[0;35m',
    'azul': '\033[0;34m'
}
num = int(input('{}Me diga um número qualquer: {}'.format(cores['roxo'], cores['limpar'])))
# Verificar se o número é PAR ou ÍMPAR
if num % 2 == 0:
    print('O número {} é {}PAR{}'.format(num, cores['azul'], cores['limpar']))
else:
    print('O número {} é {}ÍMPAR{}'.format(num, cores['azul'], cores['limpar']))

# Solução Gustavo Guanabara
'''
número = int(input('Me dige um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))
'''
