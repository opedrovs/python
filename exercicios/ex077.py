cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
am = cores['amarelo']
az = cores['azul']

# Minha solução (Não correta)
'''
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
vogais = vezes = ''
for palavra in palavras:
    if 'a' in palavra:
        vezes = palavra.count('a')
        vogais += vezes * 'a '
    if 'e' in palavra:
        vezes = palavra.count('e')
        vogais += vezes * 'e '
    if 'i' in palavra:
        vezes = palavra.count('i')
        vogais += vezes * 'i '
    if 'o' in palavra:
        vezes = palavra.count('o')
        vogais += vezes * 'o '
    if 'u' in palavra:
        vezes = palavra.count('u')
        vogais += vezes * 'u '
    print(f'Na palavra {palavra} temos {vogais}')
    vogais = ''
'''

# Solução criada apartir de um COMENTÁRIO
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'\nNa palavra {az}{palavra.upper()}{li} temos ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{am}{letra}{li} ', end='')

# Solução Gustavo Guanabara
'''
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
'''
