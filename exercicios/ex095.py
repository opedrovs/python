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
print(f'{az}<< {am}VOLTE SEMPRE {az}>>{li}')
