cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'cinza': '\033[0;37m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']
cz = cores['cinza']

# Minha solução
times = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Red Bull Bragantino',
         'Fluminense', 'America', 'Atlético', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
         'Athletico Paranaense', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(f'{az}-={li}' * 15)
print(f'Lista de times do Brasileirão: {cz}{times}')
print(f'{az}-={li}' * 15)
print(f'Os 5 primeiros são {vd}{times[:5]}{li}')
print(f'{az}-={li}' * 15)
print(f'Os 4 últimos são {vm}{times[-4:]}{li}')
print(f'{az}-={li}' * 15)
print(f'Times em ordem alfabética: {cz}{sorted(times)}')
print(f'{az}-={li}' * 15)
print(f'O Chapecoense está na {am}{times.index("Chapecoense")+1}º{li} posição')

# Solução Gustavo Guanabara
'''
times = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Red Bull Bragantino',
         'Fluminense', 'America', 'Atlético', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
         'Athletico Paranaense', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapeconese está na {times.index("Chapecoense")+1}º posição')
'''
