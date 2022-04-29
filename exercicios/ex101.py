from datetime import date


def voto(nasc):
    idade = date.today().year - nasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print(f'VOTO NEGADO.')
    elif idade < 18:
        print(f'VOTO OPCIONAL.')
    else:
        print(f'VOTO OBRIGATÓRIO.')


print('-' * 30)
anonasc = int(input('Em que ano você nasceu? '))
voto(anonasc)
