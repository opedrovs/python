# Minha solução
nome = str(input('Qual é seu nome completo? ')).strip()
nsilva = 'SILVA' in nome.upper().split()
print('Seu nome tem Silva? {}'.format(nsilva))

# Solução Gustavo Guanabara
'''
nome = input('Qual é seu nome completo? ').strip()
print("Seu nome tem Silva? {}".format('SILVA' in nome.upper()))
'''
