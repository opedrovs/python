cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
limp = cores['limpar']
amar = cores['amarelo']
azul = cores['azul']

# Minha solução


'''def ficha(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '' or gols.isalpha():
        gols = 0
    print(f'O jogador {azul}{nome}{limp} fez {amar}{gols}{limp} gol(s) no campeonato.')


print('-' * 30)
nomejog = str(input('Nome do Jogador: ')).strip()
numgols = str(input('Número de Gols: ')).strip()
print(ficha(nomejog, numgols))'''

# Solução Gustavo Guanabara


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
