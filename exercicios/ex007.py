aluno = input('Nome do aluno: ')
pri = float(input('Primeira nota de {}: '.format(aluno)))
seg = float(input('Segunda nota de {}: '.format(aluno)))
media = (pri + seg) / 2
print('A média do aluno {} é de {}.'.format(aluno, media))
