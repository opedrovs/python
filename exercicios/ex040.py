cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']

# Minha solução
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if nota1 > 10 or nota2 > 10 and nota1 < 0 or nota2 < 0:
    # ERRO: Se a nota for abaixo de 0 e acima de 10.
    print(f'{vm}Nota inválida!{li} Não aceitamos notas menores que 0 e maiores que 10.')
elif media >= 7:
    # Caso aluno tire acima de 7 (APROVADO)
    print(f'O aluno está {vd}APROVADO{li}.')
elif media >= 5:
    # Caso aluno tire entre 5 e 6.9 (RECUPERAÇÃO)
    print(f'O aluno está em {am}RECUPERAÇÃO{li}.')
else:
    # Caso aluno tire abaixo que 5 (REPROVADO)
    print(f'O aluno está {vm}REPROVADO{li}.')

# OU

'''
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
if media >= 7:
    print(f'O aluno está {vd}APROVADO{l}.')
elif media >= 5:
    print(f'O aluno está em {am}RECUPERAÇÃO{l}.')
else:
    print(f'O aluno está {vm}REPROVADO{l}.')

# Solução Gustavo Guanabara

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')
'''
