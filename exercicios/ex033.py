# Minha solução
cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'vermelho': '\033[0;31m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vd = cores['verde']
vm = cores['vermelho']
am = cores['amarelo']
rx = cores['roxo']

p = int(input('{}Primeiro valor:{} '.format(rx, li)))
s = int(input('{}Segundo valor:{} '.format(rx, li)))
t = int(input('{}Terceiro valor:{} '.format(rx, li)))

# Verificando o maior valor:
if p > s and p > t:
    maior = p
elif s > p and s > t:
    maior = s
elif t > p and t > s:
    maior = t

# Verificando o menor valor:
if p < s and p < t:
    menor = p
elif s < p and s < t:
    menor = s
elif t < p and t < s:
    menor = t

print('O {}menor{} valor informado foi {}{}{}'.format(vm, li, am, menor, li))
print('O {}maior{} valor informado foi {}{}{}'.format(vd, li, am, maior, li))

# Solução Gustavo Guanabara
'''
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor informado foi {}'.format(menor))
print('O maior valor informado foi {}'.format(maior))
'''
