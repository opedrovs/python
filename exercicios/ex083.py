cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']

expressao = []
expressao.append(str(input('Digite a expressão: ')))
for item in expressao:
    for letra in item:
        parentese1 = item.count('(')
        parentese2 = item.count(')')
if parentese1 == parentese2:
    print(f'{vd}Sua expressão está {am}válida!{li}')
else:
    print(f'{vm}Sua expressão está {am}errada!{li}')
