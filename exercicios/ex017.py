# Minha solução (tive dificuldade)
from math import sqrt, hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# hi = sqrt(co ** 2 + ca ** 2)
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# Solução Gustavo Guanabara

# Sem importação
'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''

# Com importação (Modo mais simples e prático de calcular)
'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''
