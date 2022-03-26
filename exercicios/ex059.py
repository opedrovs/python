cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}

# Minha solução
from time import sleep
pri = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
print('''   [ 1 ] soma
   [ 2 ] multiplicar
   [ 3 ] maior
   [ 4 ] novos números
   [ 5 ] sair do programa''')
opcao = int(input('>>>>> Qual é a sua opção? '))
maior = 0
sair = 0
while sair != 1:
    if opcao == 5:
        sair += 1
        print('Finalizando...')
        print('=-=' * 10)
        sleep(1.5)
    else:
        if opcao == 1:
            print(f'A soma entre {pri} + {seg} é {pri+seg}')
        elif opcao == 2:
            print(f'O resultado de {pri} x {seg} é {pri*seg}')
        elif opcao == 3:
            maior = pri
            if seg > pri:
                maior = seg
            print(f'Entre {pri} e {seg} o maior valor é {maior}')
        elif opcao == 4:
            print('Informe os números novamente:')
            pri = int(input('Primeiro valor: '))
            seg = int(input('Segundo valor: '))
        else:
            print('Opção inválida. Tente novamente')
        print('=-=' * 10)
        sleep(1.5)
        print('''   [ 1 ] soma
   [ 2 ] multiplicar
   [ 3 ] maior
   [ 4 ] novos números
   [ 5 ] sair do programa''')
        opcao = int(input('>>>>> Qual é a sua opção? '))
print('Fim do programa! Volte sempre!')
