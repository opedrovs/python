# Minha Solução
def leiaInt(msg):
    valint = 0
    while True:
        try:
            valint = int(input(msg))
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            break
        except:
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            break
    return valint


def leiaFloat(msg):
    valfloat = 0
    while True:
        try:
            valfloat = float(input(msg))
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            break
        except:
            print('\033[0;31mERRO: por favor, digite um número real válido.\033[m')
        else:
            break
    return valfloat


inteiro = leiaInt('Digite um Inteiro: ')
real = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')

# Solução Gustavo Guanabara


'''def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')'''
