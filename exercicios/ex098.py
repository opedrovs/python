# Minha solução
from time import sleep


def cont(ini, fim, passo):
    print('-=' * 20)
    if passo == 0:
        passo = 1
    while passo < 0:
       passo *= -1
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    if ini < fim:
        for c in range(ini, fim+1, passo):
            print(f'{c} ', end='')
            #sleep(0.3)
    elif ini > fim:
        for c in range(ini, fim-1, -passo):
            print(f'{c} ', end='')
            #sleep(0.3)
    print('FIM!')


cont(1, 10, 1)
cont(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
cont(int(input(f'{"Início:":<7} ')),
     int(input(f'{"Fim:":<7} ')),
     int(input(f'{"Passo:":<7} ')))
# OU podemos utilizar o ABS para converte número negativo em positivo.
# abs(int(input(f'{"Passo:":<7} '))))
