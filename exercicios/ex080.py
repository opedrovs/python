cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
am = cores['amarelo']
az = cores['azul']

# Minha solução
valores = []
for cont in range(0, 5):
    valor = int(input('Digite um valor: '))
    if cont == 0:
        valores.append(valor)
        print('Adicionado ao final da lista...')
    else:
        for pos in range(0, len(valores)):
            if valor > max(valores):
                valores.append(valor)
                print('Adicionado ao final da lista...')
                break
            elif valor < valores[pos]:
                valores.insert(pos, valor)
                print(f'Adicionado na posição {az}{pos}{li} da lista...')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {am}{valores}{li}')

# Solução Gustavo Guanabara
'''
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
'''
