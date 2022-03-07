# Minha solução
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
print('{}-={}'.format(cores['amarelo'], cores['limpa']) * 18)
print('{}Analisador de Triângulos{}'.format(cores['azul'], cores['limpa']))
print('{}-={}'.format(cores['amarelo'], cores['limpa']) * 18)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('{}Os segmentos acima {}PODEM FORMAR {}triângulo!{}'.format(cores['verde'], cores['amarelo'], cores['verde'], cores['limpa']))
else:
    print('{}Os segmentos acima {}NÃO PODEM FORMAR {}triângulo!{}'.format(cores['vermelho'], cores['amarelo'], cores['vermelho'], cores['limpa']))

# Solução Gustavo Guanabara
'''
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('OS segmentos acima NÃO PODEM FORMAR triângulo!')
'''
