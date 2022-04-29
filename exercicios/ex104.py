cores = {
    'limpar': '\033[m',
    'destaque': '\033[1;31m',
    'amarelo': '\033[0;33m'
}
li = cores['limpar']
dt = cores['destaque']
am = cores['amarelo']


def leiaInt(n):
    while True:
        n = str(input('Digite um número: '))
        if int(n.isnumeric()):
            break
        print(f'{dt}ERRO! Digite um número inteiro válido.{li}')
    return n


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {am}{n}{li}')
