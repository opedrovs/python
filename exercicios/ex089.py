geral = [[], [[], []], []]
media = pos = 0
while True:
    geral[0].append(str(input('Nome: ')))
    geral[1][0].append(float(input('Nota 1: ')))
    geral[1][1].append(float(input('Nota 2: ')))
    for aluno in geral[1]:
        for nota in aluno:
            media += nota / 2
            geral[2].append(media)
    resp = ' '
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"No. NOME":<20} {"MÉDIA"}')
print('-' * 30)
