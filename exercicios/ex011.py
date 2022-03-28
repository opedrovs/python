# Minha solução

cores = {
    'limpar': '\033[m',
    'amarelo': '\033[0;33m',
    'verde': '\033[0;32m',
    'roxo': '\033[0;35m'
}

li = cores['limpar']
a = cores['amarelo']
v = cores['verde']
r = cores['roxo']

larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = alt * larg
tinta = area / 2
print('Com largura de {}{}m{} e altura de {}{}m{}, possui uma área de {}{}m²{}.'.format(a, larg, li, a, alt, li, v, area, li))
print('Você vai precisar de {}{}l{} de tinta para pintar a parede por completo.'.format(r, tinta, li))

# Solução de Gustavo Guanabara (CursoemVideo)

# larg = float(input('Largura da parede: '))
# alt = float(input('Altura da parede: '))
# área = larg * alt
# print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
# tinta = área / 2
# print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
