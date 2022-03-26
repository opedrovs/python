# Minha solução
num = 1
soma = 0
totnum = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        num = 999
    else:
        soma += num
        totnum += 1
print(f'Você digitou {totnum} números e a soma entre eles foi {soma}.')
