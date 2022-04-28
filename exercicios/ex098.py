# Minha solução
from time import sleep


def contador(ini, fim, passo):
    print('-=' * 20)
    if passo == 0:
        passo = 1
    while passo < 0:
        passo *= -1
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    sleep(1.5)
    if ini < fim:
        for c in range(ini, fim + 1, passo):
            print(f'{c} ', end='')
            sleep(0.3)
    elif ini > fim:
        for c in range(ini, fim - 1, -passo):
            print(f'{c} ', end='')
            sleep(0.3)
    print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input(f'{"Início:":<7} ')),
         int(input(f'{"Fim:":<7} ')),
         int(input(f'{"Passo:":<7} ')))
# OU podemos utilizar o ABS para converte número negativo em positivo.
# abs(int(input(f'{"Passo:":<7} '))))


# Solução Gustavo Guanabara


'''def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print(f'FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('FIm:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)'''
