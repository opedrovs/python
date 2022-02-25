# Minha solução
# m = float(input('Digite um valor em metro(m): '))
# cm = m * 100
# mm = m * 1000
# print('{} metros(m), é igual a {:.0f} centímetros(cm) e {:.0f} milímetros(mm).'.format(m, cm, mm))

# Minha segunda solução após ver o video do CursoemVideo
m = float(input('Uma distância em metros: '))
print('A medida de {:.1f}m corresponde a'.format(m))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(km, hm, dam, dm, cm, mm))

# Solução Gustavo Guanabara (CursoemVideo)

# medida = float(input('Uma distância em metros: '))
# cm = medida * 100
# mm = medida * 1000
# print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
