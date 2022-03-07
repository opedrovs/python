# Minha solução
cores = {
    'limpar': '\033[m',
    'azul': '\033[0;34m'
}
nome = str(input('Qual é seu nome completo? ')).strip()
nsilva = 'SILVA' in nome.upper().split()
print('Seu nome tem Silva? {}{}{}'.format(cores['azul'], nsilva, cores['limpar']))

# Solução Gustavo Guanabara
'''
nome = input('Qual é seu nome completo? ').strip()
print("Seu nome tem Silva? {}".format('SILVA' in nome.upper()))
'''
