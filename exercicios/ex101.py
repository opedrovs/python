cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']

# Minha solução após ver o resultado


def voto(nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return f'NÃO VOTA.'
    elif idade < 18 or idade > 65:
        return f'VOTO OPCIONAL.'
    else:
        return f'VOTO OBRIGATÓRIO.'


anonasc = int(input('Em que ano você nasceu? '))
print(voto(anonasc))


# Minha solução
'''
from datetime import date


def voto(nasc):
    atual = date.today().year
    idade = atual - nasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return print(f'{vm}NÃO VOTA{li}.')
    elif idade < 18 or idade > 65:
        return print(f'{am}VOTO OPCIONAL{li}.')
    else:
        return print(f'{vd}VOTO OBRIGATÓRIO{li}.')


print('-' * 30)
anonasc = int(input('Em que ano você nasceu? '))
voto(anonasc)'''

# Solução Gustavo Guanabara
# Melhor maneiro, assim, econômiza memória (colocando o import dentro da função)
# Assim ela só é executada dentro da função


'''def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))'''
