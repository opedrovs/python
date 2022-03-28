# Minha solução
cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
rx = cores['roxo']
am = cores['amarelo']

frase = str(input('Digite uma frase: ')).strip()
print('A letra {}A{} aparece {}{}{} vezes na frase.'.format(am, li, rx, frase.lower().count('a'), li))
print('A primeira letra {}A{} apareceu na posição {}{}{}'.format(am, li, rx, frase.lower().find('a')+1, li))
print('A última letra {}A{} apareceu na posição {}{}{}'.format(am, li, rx, frase.lower().rfind('a')+1, li))

# ou

'''
frase = str(input('Digite uma frase: ')).strip()
letra = frase.lower().count('a')
print(f'A letra A aparece {letra} vezes na frase.')
prim = frase.lower().find('a')+1
print(f'A primeira letra A apareceu na posição {prim}')
ult = frase.lower().rfind('a')+1
print(f'A última letra A apareceu na posição {ult}')
'''

# Solução Gustavo Guanabara
'''
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
'''
