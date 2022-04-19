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

# Minha solução (Não correta)
'''
expres = []
paberto = pfechado = 0
pri = ''
expres.append(str(input('Digite a expressão: ')))
for e in expres:
    paberto = e.count('(')
    pfechado = e.count(')')
if paberto == pfechado and e[0] != ')':
    print(f'{vd}Sua expressão está {am}válida!{li}')
else:
    print(f'{vm}Sua expressão está {am}errada!{li}')
'''

# Solução Gustavo Guanabara
expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
