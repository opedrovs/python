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
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print(f'Você digitou os valores {am}{valores}{li}')
print('=-' * 30)
maior = max(valores)
menor = min(valores)
print(f'O maior valor digitado foi {vd}{maior}{li} nas posições ', end='')
for pos in range(0, len(valores)):
    if valores[pos] == maior:
        print(f'{az}{pos}{li}... ', end='')
print(f'\nO menor valor digitado foi {vm}{menor}{li} nas posições ', end='')
for pos in range(0, len(valores)):
    if valores[pos] == menor:
        print(f'{az}{pos}{li}... ', end='')
