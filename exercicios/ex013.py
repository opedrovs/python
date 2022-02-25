# Minha solução
nome = input('Nome do funcionário: ')
sal = float(input('Salário atual de {}, R$'.format(nome)))
porcen = (sal / 100) * 15
aumento = porcen + sal
print('O salário de {} era de R$ {:.2f}, agora com o aumento de 15%, passará a ganhar R$ {:.2f}.'.format(nome, sal, aumento))

# Solução Gustavo Guanabara CursoemVideo
# salário = float(input('Qual é o salário do Funcionário? R$'))
# novo = salário + (salário * 15 / 100)
# print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))

