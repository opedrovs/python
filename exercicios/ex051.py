cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
l = cores['limpar']
am = cores['amarelo']
az = cores['azul']

# Minha solução
print(f'{az}={l}'*28)
print(f'{am}{"10 TERMOS DE UMA PA":^28}{l}')
print(f'{az}={l}'*28)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
valor = 0
for cont in range(1, 11):
    print(f'{am}{pri+valor}{l}', end=f' → ')
    valor += razao
print(f'{az}ACABOU{l}')
