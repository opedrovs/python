from time import sleep
from random import randint

cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

# Minha solução


'''def maior(* valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in valores:
        print(f'{am}{valor}{li} ', end='')
        sleep(0.3)
    print(f'Foram informados {az}{len(valores)}{li} valores ao todo.')
    if len(valores) == 0:
        print(f'O maior valor informado foi {vd}0{li}.')
    else:
        print(f'O maior valor informado foi {vd}{max(valores)}{li}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''

# Minha outra solução com números aleatórios


'''def maior(* valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in valores:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(valores)} valores ao todo.')
    if len(valores) == 0:
        print('O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(valores)}.')


# Programa Principal
maior(randint(1, 9), randint(1, 9), randint(1, 9),
      randint(1, 9), randint(1, 9), randint(1, 9))
maior(randint(1, 9), randint(1, 9), randint(1, 9))
maior(randint(1, 9), randint(1, 9))
maior(randint(1, 9))
maior()'''

# Solução Gustavo Guanabara


def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
