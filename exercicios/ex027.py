# Minha solução

cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m'
}

nome = str(input('Digite seu nome completo: ')).split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}{}{}'.format(cores['verde'], nome[0], cores['limpar']))
print('Seu último nome é {}{}{}'.format(cores['verde'], nome[-1], cores['limpar']))

# Solução Gustavo Guanabara
'''
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
'''
