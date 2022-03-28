from time import sleep
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']
rx = cores['roxo']

# Minha solução
pri = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
print(f'''   [ {rx}1{li} ] soma
   [ {rx}2{li} ] multiplicar
   [ {rx}3{li} ] maior
   [ {rx}4{li} ] novos números
   [ {rx}5{li} ] sair do programa''')
opcao = int(input(f'{az}>>>>>{li} Qual é a sua opção? '))
maior = 0
sair = 0
while sair != 1:
    if opcao == 5:
        print(f'{rx}Finalizando...{li}')
        print('=-=' * 10)
        sleep(1.5)
        sair += 1
    else:
        if opcao == 1:
            print(f'A soma entre {vd}{pri} + {seg}{li} é {am}{pri+seg}{li}')
        elif opcao == 2:
            print(f'O resultado de {vd}{pri} x {seg}{li} é {am}{pri*seg}{li}')
        elif opcao == 3:
            maior = pri
            if seg > pri:
                maior = seg
            print(f'Entre {vd}{pri}{li} e {vd}{seg}{li} o maior valor é {am}{maior}{li}')
        elif opcao == 4:
            print('Informe os números novamente:')
            pri = int(input('Primeiro valor: '))
            seg = int(input('Segundo valor: '))
        else:
            print(f'{vm}Opção inválida. Tente novamente{li}')
        print('=-=' * 10)
        sleep(1.5)
        print(f'''   [ {rx}1{li} ] soma
   [ {rx}2{li} ] multiplicar
   [ {rx}3{li} ] maior
   [ {rx}4{li} ] novos números
   [ {rx}5{li} ] sair do programa''')
        opcao = int(input(f'{az}>>>>>{li} Qual é a sua opção? '))
print(f'{vd}Fim do programa! Volte sempre!{li}')
