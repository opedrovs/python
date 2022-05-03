def leiaDinheiro(valor):
    while True:
        valor = str(input('Digite o preço: R$')).strip()
        if valor.replace('.', '0') or valor.replace(',', '0').isnumeric():
            return float(valor.replace(',', '.'))
        print(f'\033[0;31mERRO: "{valor}" é um preço inválido!\033[m')
