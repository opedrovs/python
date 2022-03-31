cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'cinza': '\033[0;37m'
}
li = cores['limpar']
vm = cores['vermelho']
am = cores['amarelo']
az = cores['azul']
cz = cores['cinza']

# Minha solução após ver resposta
print(f'{am}Gerador de PA{li}')
print(f'{az}-={li}' * 10)
pri = int(input(f'Primeiro termo: '))
raz = int(input(f'Razão da PA: '))
termo = pri
cont = 1
while cont <= 10:
    print(f'{termo} {cz}→{li}', end=' ')
    termo += raz
    cont += 1
print(f'{vm}FIM{li}')

# Minha solução
'''
print('Gerador de PA')
print('-=' * 12)
pri = int(input(f'{rx}Primeiro termo:{li} '))
raz = int(input(f'{rx}Razão da PA:{li} '))
cont = 1
while cont <= 10:
        print(f'{am}{pri}{li}', end=' → ')
        pri += raz
        cont += 1
print(f'{vm}FIM{li}')
'''

# Solução Gustavo Guanabara
'''
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
'''
