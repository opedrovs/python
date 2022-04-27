cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']

# Minha solução
cadastro = {}
lgols = []
tot = 0
lista = []
while True:
    lgols = []
    tot = 0
    cadastro['nome'] = str(input('Nome do Jogador: '))
    quant = int(input(f'Quantas partidas {am}{cadastro["nome"]}{li} jogou? '))
    for part in range(0, quant):
        gol = int(input(f'   Quantos gols na partida {part+1}? '))
        lgols.append(gol)
        tot += gol
    cadastro['gols'] = lgols
    cadastro['total'] = tot
    lista.append(cadastro.copy())
    resp = ' '
    while resp != 'S' and resp != 'N':
        resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"cód nome":<16}', f'{"gols":<16}', f'{"total"}')
print('-' * 40)
for pos, jog in enumerate(lista):
    print(f'{am}{pos:>3}{li} {jog["nome"]:<12} {az}{str(jog["gols"]):<16} {vd}{jog["total"]}{li}')
while True:
    print('-' * 40)
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod == 999:
        break
    else:
        if cod > len(lista)-1 or cod < 0:
            print(f'{vm}ERRO! Não existe jogador com código {am}{cod}!{li}')
        else:
            print(f' -- LEVANTAMENTO DO JOGADOR {am}{lista[cod]["nome"]}{li}:')
            for ind, jog in enumerate(lista[cod]["gols"]):
                print(f'    No jogo {ind+1} fez {vd}{jog}{li} gols.')
print(f'{am}<< {az}VOLTE SEMPRE {am}>>{li}')

# Solução Gustavo Guanabara
'''
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
print('-=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
        print('-' * 40)
print('<< VOLTE SEMPRE >>')'''
