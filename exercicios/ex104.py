cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'amarelo': '\033[0;33m'
}
li = cores['limpar']
vm = cores['vermelho']
am = cores['amarelo']

# Minha solução


'''def leiaInt(num):
    print('-' * 30)
    while True:
        num = str(input('Digite um número: ')).strip()
        if int(num.isnumeric()):
            break
        print(f'{vm}ERRO! Digite um número inteiro válido.{li}')
    return num


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {am}{n}{li}')'''

# Solução Gustavo Guanabara


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

