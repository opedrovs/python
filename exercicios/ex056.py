mulheres = 0
homens = 0
velho = 0
media = 0
for cont in range(1, 5):
    print(f'{f" {cont}º PESSOA " :-^21}')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')

    if sexo == 'M':
        if mulheres <= 20:
            mulheres += 1
    elif sexo == 'F':
        if homens > velho:
            vnome = nome
            vidade = velho

    media += idade / 4


print(f'A média de idade do grupo é de {media} anos')
# print(f'O homem mais velho tem {} anos e se chama {}.')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos.')
