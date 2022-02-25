nome = input('Nome do funcionário: ')
sal = float(input('Salário atual de {}, R$'.format(nome)))
porcen = (sal / 100) * 15
aument = porcen + sal
print('O salário de {} era de R$ {:.2f}, agora com o aumento de 15%, passará a ganhar R$ {:.2f}.'.format(nome, sal, aument))
