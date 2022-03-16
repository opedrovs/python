import emoji
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('BUM! BUM! POOOW! :fireworks:', use_aliases=True))
