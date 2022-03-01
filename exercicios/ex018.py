# Minha solução (tive dificuldade)
from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
rad = radians(ang)
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sin(rad)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos(rad)))
print('O ângulo de {} tem o TARGENTE de {:.2f}'.format(ang, tan(rad)))

# Solução de Gustavo Guanabara
'''
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ângulo, tangente))
'''
