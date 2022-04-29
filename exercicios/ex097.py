cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
am = cores['amarelo']
az = cores['azul']

# Minha Solução


def escreva(txt):
    tam = len(txt)
    print(f'{az}~' * tam)
    print(f'{am}{txt}')
    print(f'{az}~{li}' * tam)


# Programa Principal
escreva(' Gustavo Guanabara ')
escreva(' Curso de Python no YouTube ')
escreva(' CeV ')
escreva(' Olá, Mundo! ')

# Solução Gustavo Guanabara


'''def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')'''
