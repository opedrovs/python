def ficha(n='', g=''):
    if n == '':
        n = '<desconhecido>'
    if g == '' or g.isalpha():
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


print('-' * 30)
nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: ')).strip()
ficha(nome, gols)
