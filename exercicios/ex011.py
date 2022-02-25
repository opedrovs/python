larg = int(input('Qual a largura da parede em metros? '))
alt = int(input('Qual a altura da parede em metros? '))
area = alt * larg
tinta = area / 2
print('Com largura de {}m e altura de {}m, possui uma área de {}m.'.format(larg, alt, area))
print('Cada litro de tinta, pinta 2m, então vai precisar de {} litros de tinta para pintar a parede por completo.'.format(tinta))
