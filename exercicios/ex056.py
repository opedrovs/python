cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

# Minha solução

media = 0
listahomens = []
velhoidade = 0
velhonome = '-'
listamulheres = []
totalm = 0
for cont in range(1, 5):
    print(f'{am}{f" {az}{cont}º PESSOA{am} ":-^35}{li}')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade / 4
    if sexo == 'M':
        # Sexo Masculino (M)
        listahomens += [nome, idade, sexo]
        if idade > velhoidade:
            # Homem mais velho (IDADE e NOME)
            velhoidade = idade
            velhonome = nome
    elif sexo == 'F':
        # Sexo Feminino (F)
        listamulheres += [nome, idade, sexo]
        if idade < 20:
            # Mulheres que tem menos de 20 anos (quantas)
            totalm += 1
    else:
        # Sexo inválido!
        print('[ERRO] Sexo inválido. Desconsiderado!')
print(f'A média de idade do grupo é de {az}{media:.1f} anos{li}')
if velhoidade == 0:
    pass
else:
    print(f'O homem mais velho tem {vd}{velhoidade} anos{li} e se chama {vd}{velhonome}{li}.')
if totalm == 0:
    pass
else:
    print(f'Ao todo são {am}{totalm} mulheres{li} com menos de 20 anos.')

# Solução Gustavo Guanabara:
'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}º PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.1f} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
'''
