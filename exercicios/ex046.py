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

# Minha solução
'''
import emoji
from time import sleep
for c in range(10, -1, -1):
    print(f'{am}{c}{l}')
    sleep(1)
print(emoji.emojize(f'{vm}BUM! BUM! POOOW! :fireworks:{l}', use_aliases=True))
'''

import emoji
from time import sleep
for c in range(10, -1, -1):
    sleep(1)
    if c >= 7:
        print(f'{vd}{c}{l}')
    elif c >= 3:
        print(f'{am}{c}{l}')
    else:
        print(f'{vm}{c}{l}')
print(emoji.emojize(f'{vm}BUM! {am}BUM! {vm}POOOW! :fireworks:{l}', use_aliases=True))
