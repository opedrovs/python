cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
l = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

# Minha solução
listahomens = []
velhoidade = 0
velhonome = '-'
listamulheres = []
totalm = 0
media = 0
for cont in range(1, 5):
    print(f'{am}{f" {az}{cont}º PESSOA{am} ":-^35}{l}')
    # print(f'{az}{f" {cont}º PESSOA ":-^21}{l}')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
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

    media += idade / 4
print(f'A média de idade do grupo é de {az}{media:.1f} anos{l}')
print(f'O homem {vd}mais{l} velho tem {am}{velhoidade} anos{l} e se chama {am}{velhonome}{l}.')
print(f'Ao todo são {am}{totalm} mulheres{l} com {vm}menos{l} de 20 anos.')
