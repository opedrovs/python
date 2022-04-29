# Minha solução
from time import sleep

cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;30;41m',
    'branco': '\033[7;40m',
    'verde': '\033[0;30;42m',
    'azul': '\033[7;34;40m'
}
limp = cores['limpar']
branco = cores['branco']
verm = cores['vermelho']
verd = cores['verde']
azul = cores['azul']


def titulo(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


def ajuda(comando):
    print(f'{branco}', end='')
    return help(f'{comando}')


while True:
    print(f'{verd}', end='')
    titulo('SISTEMA DE AJUDA PyHELP')
    print(f'{limp}', end='')
    cmd = str(input('Função ou Biblioteca > '))
    if cmd.upper() == 'FIM':
        print(f'{verm}', end='')
        titulo('ATÉ LOGO!')
        sleep(1.5)
        break
    print(f'{azul}', end='')
    titulo(f"Acessando o manual do comando '{cmd}'")
    print(f'{limp}', end='')
    sleep(1.5)
    ajuda(cmd)
    sleep(1.5)
