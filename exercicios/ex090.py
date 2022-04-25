cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['média'] = float(input(f'Média de {cadastro["nome"]}: '))
if cadastro['média'] >= 7:
    cadastro['situação'] = 'Aprovado'
elif cadastro['média'] >= 5:
    cadastro['situação'] = 'Recuperação'
else:
    cadastro['situação'] = 'Reprovado'
print('-=' * 30)
for chave, aluno in cadastro.items():
    print(f'  - {chave} é igual a {aluno}')

