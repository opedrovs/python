# Minha solução
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'roxo': '\033[0;35m'
}
l = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
am = cores['amarelo']
az = cores['azul']
rx = cores['roxo']

# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
loja = f' {az}LOJAS GUANABARA{l} '
print(f'{loja:=^42}')
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print(f'[ {rx}1{l} ] á vista dinheiro/cheque')
print(f'[ {rx}2{l} ] á vista cartão')
print(f'[ {rx}3{l} ] 2x no cartão')
print(f'[ {rx}4{l} ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    # Pagamento á vista dinheiro/cheque
    precofinal = preco - (preco * 10 / 100)
elif opcao == 2:
    # Pagamento á vista cartão
    precofinal = preco - (preco * 5 / 100)
elif opcao == 3:
    # Pagamento parcelado em 2x
    precoparcela = preco / 2
    precofinal = preco
    print(f'Sua compra será parcelada em {am}2x{l} de {am}R${precoparcela:.2f}{l} SEM JUROS')
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    # Pagamento parcelado em 3x ou mais
    if parcela == 2:
        # Pagamento parcelado em 2x
        precoparcela = preco / 2
        precofinal = preco
        print(f'Sua compra será parcelada em {am}2x{l} de {am}R${precoparcela:.2f}{l} SEM JUROS')
    elif parcela == 1:
        # Pagamento parcelado em 1x
        precofinal = preco - (preco * 5 / 100)
    else:
        # Pagamento parcelado em 3x ou mais
        precofinal = preco + (preco * 20 / 100)
        precoparcela = precofinal / parcela
        print(f'Sua compra será parcelada em {am}{parcela}x{l} de {am}R${precoparcela:.2f}{l} COM JUROS')
else:
    # Nenhuma das 4 opções de pagamento
    precofinal = preco
    print(f'{vm}[ERRO] Opção inválida de pagamento. Tente novamente!{l}')
print(f'Sua compra de {vm}R${preco:.2f}{l} vai custar {vd}R${precofinal:.2f}{l} no final.')

# Solução Gustavo Guanabara
# print('{:=^40}'.format(' LOJAS GUANABARA '))
# preço = float(input('Preço das compras: R$'))
# print('''FORMAS DE PAGAMENTO
# [ 1 ] á vista dinheiro/cheque
# [ 2 ] á vista cartão
# [ 3 ] 2x no cartão
# [ 4 ] 3x ou mais no cartão''')
# opção = int(input('Qual é a opção? '))
# if opção == 1:
#     total = preço - (preço * 10 / 100)
# elif opção == 2:
#     total = preço - (preço * 5 / 100)
# elif opção == 3:
#     total = preço
#     parcela = preço / 2
#     print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
# elif opção == 4:
#     total = preço + (preço * 20 / 100)
#     totparc = int(input('Quantas parcelas? '))
#     parcela = total / totparc
#     print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
# else:
#     total = preço
#     print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
# print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
