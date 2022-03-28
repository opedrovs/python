# Minha solução
cores = {
    'limpar': '\033[m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'roxo': '\033[0;35m'
}
li = cores['limpar']
vm = cores['vermelho']
vd = cores['verde']
rx = cores['roxo']

sal = float(input('{}Qual é o salário do funcionário? {}R${}'.format(rx, vd, li)))
if sal >= 1250:
    # Novo salário com 10% de aumento
    aumento = sal + (sal * 10) / 100
else:
    # Novo salário com 15% de aumento
    aumento = sal + (sal * 15) / 100
print('Quem ganhava {}R${:.2f}{} passa a ganhar {}R${:.2f}{} agora.'.format(vm, sal, li, vd, aumento, li))

# Solução Gustavo Guanabara
'''
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
'''
