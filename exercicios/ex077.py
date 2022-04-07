# AINDA FAZENDO
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
