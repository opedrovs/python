cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
vm = cores['vermelho']
am = cores['amarelo']
az = cores['azul']

# Minha solução após ver a resposta:
print(f'{az}={li}'*28)
print(f'{am}{"10 TERMOS DE UMA PA":^28}{li}')
print(f'{az}={li}'*28)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = pri + (10 - 1) * raz
for c in range(pri, dec + raz, raz):
    print(f'{am}{c}{li}', end=' → ')
print(f'{az}ACABOU{li}')

# Minha solução
'''
print(f'{az}={l}'*28)
print(f'{am}{"10 TERMOS DE UMA PA":^28}{l}')
print(f'{az}={l}'*28)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
valor = 0
if razao == 0:
    print(f'{vm}[ERRO] Razão inválida!{l}')
else:
    for cont in range(1, 11):
        print(f'{am}{pri + valor}{l}', end=' → ')
        valor += razao
    print(f'{az}ACABOU{l}')
'''

# Solução Gustavo Guanabara:
'''
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(c, end=' → ')
print('ACABOU')
'''
