# Minha solução, com ajuda: https://www.geeksforgeeks.org/python-urllib-module/

from urllib import request
try:
    acessar = request.urlopen('http://www.pudim.com.br')
except:
    print('\033[0;31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[0;32mConsegui acessar o site Pudim com sucesso!\033[m')

# Solução Gustavo Guanabara

'''import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())  # Ler o conteúdo HTML do site'''
