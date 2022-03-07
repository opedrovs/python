# Minha outra solução (SIMPLIFICADO)
cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'roxo': '\033[0;35m'
}
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}{}{}'.format(cores['verde'], nome.upper(), cores['limpar']))
print('Seu nome em minúsculas é {}{}{}'.format(cores['verde'], nome.lower(), cores['limpar']))
separado = nome.split()
juntando = ''.join(separado)
print('Seu nome tem ao todo {}{}{} letras'.format(cores['roxo'], len(juntando), cores['limpar']))
print('Seu primeiro nome é {}{}{} e ele tem {}{}{} letras'.format(cores['verde'], separado[0], cores['limpar'], cores['roxo'], len(separado[0]), cores['limpar']))

# Minha solução
'''
nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
maius = nome.upper()
print('Seu nome em maiúsculas é {}'.format(maius))
minus = nome.lower()
print('Seu nome em minúsculas é {}'.format(minus))
nomecomp = nome.split()
todo = ''.join(nomecomp)
print('Seu nome tem ao todo {} letras'.format(len(todo)))
pnome = nomecomp[0]
print('Seu primeiro nome é {} e ele tem {} letras'.format(pnome, len(pnome)))
'''
# Solução Gustavo Guanabara
'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
'''
