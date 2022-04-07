extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num > 20 or num < 0:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[num]}')
