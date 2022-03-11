# Minha solução
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m'
}

l = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

if media >= 7:
    print(f'O aluno está {vd}APROVADO{l}.')
elif media >= 5:
    print(f'O aluno está em {am}RECUPERAÇÃO{l}.')
else:
    print(f'O aluno está {vm}REPROVADO{l}.')
