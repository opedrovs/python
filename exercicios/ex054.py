from datetime import date
# Minha solução
atual = date.today().year
maior = 0
menor = 0
for cont in range(1, 8):
    nasc = int(input(f'Em que ano a {cont}º pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
