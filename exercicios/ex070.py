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
print(f'{am}-{li}'*35)
print(f'{az}{f"LOJA SUPER BARATÃO":^35}{li}')
print(f'{am}-{li}'*35)
totcompra = produtocaro = precobarato = tot = 0
nomebarato = ''
while True:
    tot += 1
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).upper().strip()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input(f'Quer continuar? [{vd}S{li}/{vm}N{li}] ')).upper().strip()[0]
    totcompra += preco
    if preco > 1000:
        produtocaro += 1
    if tot == 1:
        precobarato = preco
        nomebarato = produto
    if preco < precobarato:
        precobarato = preco
        nomebarato = produto
    if resp == 'N':
        break
print(f'{az}{f" {am}FIM DO PROGRAMA{az} ":-^49}{li}')
print(f'O total da compra foi {vd}R${totcompra:.2f}{li}')
if produtocaro > 1:
    print(f'Temos {am}{produtocaro}{li} produtos custando mais de R$1000.00')
else:
    print(f'Temos {am}{produtocaro}{li} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {az}{nomebarato}{li} que custa {az}R${precobarato:.2f}{li}')
