def leiaDinheiro(valor=0):
    while True:
        valor = str(input('Digite o preço: \033[0;33mR$\033[m')).strip()
        if valor.replace(',', '0').isnumeric() or valor.replace('.', '0').isnumeric():
            return float(valor.replace(',', '.'))
        print(f'\033[0;31mERRO: "{valor}" é um preço inválido!\033[m')
