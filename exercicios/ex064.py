cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vd = cores['verde']
am = cores['amarelo']
rx = cores['roxo']

# Minha solução
num = 1
soma = 0
totnum = 0
while num != 999:
    num = int(input(f'Digite um número [{rx}999 para parar{li}]: '))
    if num == 999:
        num = 999
    else:
        soma += num
        totnum += 1
print(f'Você digitou {am}{totnum}{li} números e a soma entre eles foi {vd}{soma}{li}.')
