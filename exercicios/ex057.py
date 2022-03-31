cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
az = cores['azul']
rx = cores['roxo']

# Minha solução
sexo = str(input(f'Informe o seu sexo: [{az}M{li}/{rx}F{li}] ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input(f'{vm}Dados inválidos.{li} Por favor, informe seu sexo: ')).upper().strip()[0]
if sexo == 'M':
    print(f'Sexo {az}{sexo}{li} registrado com {vd}sucesso{li}')
else:
    print(f'Sexo {rx}{sexo}{li} registrado com {vd}sucesso{li}')

# Solução Gustavo Guanabara
'''
sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
'''
