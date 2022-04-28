# Minha solução
print(' Controle de Terrenos ')
print('-' * 22)


def área(comp, alt):
    calc = comp * alt
    print(f'A área de um terreno {comp:.1f}x{alt:.1f} é de {calc:.1f}m².')


área(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
