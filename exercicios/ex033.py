# Minha solução
cores = {
    'limpa': '\033[m',
    'verde': '\033[0;32m',
    'vermel': '\033[0;31m',
    'amarelo': '\033[0;33m'
}
p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: '))

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

print('O {}menor{} valor informado foi {}{}{}'.format(cores['vermel'], cores['limpa'], cores['amarelo'], menor, cores['limpa']))
print('O {}maior{} valor informado foi {}{}{}'.format(cores['verde'], cores['limpa'], cores['amarelo'], maior, cores['limpa']))

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
