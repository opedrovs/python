# primt('OI')     # Erro de sintaxe

#  ----

# print(x)    # Erro de exceção/semântica (NameError)

#   ----

# n = int(input('Número: '))
# print(f'Você digitou o número {n}')    # Erro de exceção, erro de valor (ValueError)

#   ----

# a = int(input('Numerador: '))   # Exemplo: 8
# b = int(input('Denominador: '))     # Exemplo: 0
# r = a / b
# print(f'O resultado é {r}')     # Exceção, erro de divisão por 0 (ZeroDivisionError)

# Tratamento de erros com (Try, Except, Else, Finally)

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
