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

geral = []
dados = []
notas = []
media = pos = 0
while True:
    dados.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    for notas in notas:
        media += notas / 2
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
print(f'{"No. NOME":<16} {"MÉDIA"}')
print('-' * 25)
for aluno in geral:
    print(f'{am}{pos:<3}{li} {aluno[0]:<13} {az}{aluno[1]:>4.1f}{li}')
    pos += 1
while True:
    print('-' * 35)
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        print('FINALIZANDO...')
        sleep(2.5)
        break
    print(f'Notas de {az}{geral[mostrar][0]}{li} são {am}{geral[mostrar][2]}{li}')
print(f'{am}<<< {az}VOLTE SEMPRE {am}>>>{li}')
