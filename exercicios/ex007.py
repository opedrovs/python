# Minha solução
cores = {
    'limpar': '\033[m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}

l = cores['limpar']
v = cores['verde']
am = cores['amarelo']
az = cores['azul']

aluno = input('Nome do aluno: ')
pri = float(input('Primeira nota de {}{}{}: '.format(v, aluno, l)))
seg = float(input('Segunda nota de {}{}{}: '.format(v, aluno, l)))
media = (pri + seg) / 2
print('A média entre {}{:.1f}{} e {}{:.1f}{} do aluno {}{}{} é de {}{:.1f}{}.'.format(az, pri, l, az, seg, l, v, aluno, l, am, media, l))

# Solução Gustavo Guanabara (CursoemVideo)
# n1 = float(input('Primeira nota do aluno: '))
# n2 = float(input('Segunda nota do aluno: '))
# média = (n1 + n2) / 2
# print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))
