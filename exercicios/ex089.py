from time import sleep

cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

# Minha solução
'''
geral = []
dados = []
notas = []
media = pos = 0
while True:
    dados.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    for nota in notas:
        media += nota / 2
    dados.append(media)
    media = 0
    dados.append(notas[:])
    geral.append(dados[:])
    notas.clear()
    dados.clear()
    resp = ' '
    while resp != 'S' and resp != 'N':
        resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<13} {"MÉDIA"}')
print('-' * 25)
for aluno in geral:
    print(f'{am}{pos:<3}{li} {aluno[0]:<14} {az}{aluno[1]:>4.1f}{li}')
    pos += 1
while True:
    print('-' * 35)
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        print('FINALIZANDO...')
        sleep(2)
        break
    if mostrar < 0 or mostrar >= pos:
        print(f'{vm}Aluno não encontrado! Tente novamente!{li}')
    else:
        print(f'Notas de {az}{geral[mostrar][0]}{li} são {am}{geral[mostrar][2]}{li}')
print(f'{az}<<< {am}VOLTE SEMPRE {az}>>>{li}')'''

# Solução Gustavo Guanabara
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
