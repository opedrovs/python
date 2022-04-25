cadastro = {}
lgols = []
tot = 0
cadastro['nome'] = str(input('Nome do Jogador: '))
quant = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
for part in range(0, quant):
    gol = int(input(f'   Quantos gols na partida {part}? '))
    lgols.append(gol)
    tot += gol
cadastro['gols'] = lgols
cadastro['total'] = tot
print('-=' * 30)
print(cadastro)
print('-=' * 30)
for chave, valor in cadastro.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 30)
print(f'O jogador {cadastro["nome"]} jogou {len(lgols)} partidas.')
for pos, gol in enumerate(lgols):
    print(f'    => Na partida {pos}, fez {gol} gols.')
print(f'Foi um total de {cadastro["total"]} gols.')
