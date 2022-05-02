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

# Solução Gustavo Guanabara

'''from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m')      # 6 - branco


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)'''
