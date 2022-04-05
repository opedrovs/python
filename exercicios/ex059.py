from time import sleep
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'cinza': '\033[0;37m',
    'backgroundamarelo': '\033[7;33m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']
cz = cores['cinza']
bam = cores['backgroundamarelo']

# Minha solução
pri = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
maior = 0
opcao = 0
while opcao != 5:
    print(f'''   {am}[ 1 ]{li} {az}soma{li}
   {am}[ 2 ]{li} {az}multiplicar{li}
   {am}[ 3 ]{li} {az}maior{li}
   {am}[ 4 ]{li} {az}novos números{li}
   {am}[ 5 ]{li} {az}sair do programa{li}''')
    opcao = int(input(f'>>>>> Qual é a sua opção? '))
    if opcao == 5:
        print(f'{cz}Finalizando...{li}')
        print('=-=' * 10)
        sleep(1.8)
    else:
        if opcao == 1:
            print(f'A soma entre {vd}{pri} + {seg}{li} é {bam}{pri+seg}{li}')
        elif opcao == 2:
            print(f'O resultado de {vd}{pri} x {seg}{li} é {bam}{pri*seg}{li}')
        elif opcao == 3:
            if pri > seg or seg > pri:
                if pri > seg:
                    maior = pri
                elif seg > pri:
                    maior = seg
                print(f'Entre {vd}{pri}{li} e {vd}{seg}{li} o maior valor é {bam}{maior}{li}')
            else:
                print(f'Entre {vd}{pri}{li} e {vd}{seg}{li} ambos valores são {bam}IGUAIS{li}')
        elif opcao == 4:
            print('Informe os números novamente:')
            pri = int(input('Primeiro valor: '))
            seg = int(input('Segundo valor: '))
        else:
            print(f'{vm}Opção inválida. Tente novamente{li}')
        print('=-=' * 10)
        sleep(1.8)
print(f'{vd}Fim do programa! Volte sempre!{li}')

# Solução Gustavo Guanabara
# n1 = int(input('Primeiro valor: '))
# n2 = int(input('Segundo valor: '))
# opção = 0
# while opção != 5:
#     print('''    [ 1 ] somar
#     [ 2 ] multiplicar
#     [ 3 ] maior
#     [ 4 ] novos números
#     [ 5 ] sair do programa''')
#     opção = int(input('>>>>> Qual é a sua opção? '))
#     if opção == 1:
#         soma = n1 + n2
#         print('A soma entre {} + {} é {}'.format(n1, n2, soma))
#     elif opção == 2:
#         produto = n1 * n2
#         print('O resultado de {} x {} é {}'.format(n1, n2, produto))
#     elif opção == 3:
#         if n1 > n2:
#             maior = n1
#         else:
#             maior = n2
#         print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
#     elif opção == 4:
#         print('Informe os números novamente:')
#         n1 = int(input('Primeiro valor: '))
#         n2 = int(input('Segundo valor: '))
#     elif opção == 5:
#         print('Finalizando...')
#     else:
#         print('Opção inválida. Tente novamente')
#     print('-=-'*10)
#     sleep(2)
# print('Fim do programa! Volte sempre!')
