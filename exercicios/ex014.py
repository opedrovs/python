cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
am = cores['amarelo']
rx = cores['roxo']

# Minha solução
c = float(input('Informe a temperatura em ºC: '))
f = (c * 1.8) + 32
print('A temperatura de {}{}ºC{} corresponde a {}{}ºF{}!'.format(rx, c, li, am, f, li))

# Solução Gustavo Guanabara (CursoemVideo)
# c = float(input('Informe a temperatura em ºC: '))
# f = 9 * c / 5 + 32
# OU
# f = ((9 * c) / 5) + 32
# print('A temperatura de {}ºC corresponde a {}ºF'.format(c, f))
