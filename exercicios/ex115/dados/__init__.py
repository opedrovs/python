def titulo(txt):
    print('-' * 40)
    print(txt.center(40))
    print('-' * 40)


def adicionar(nome, idade):
    novocad = list()
    novocad.append(f'{nome:<28} {idade} anos\n')
    arquivo = open('dados/cadastro', 'a')
    arquivo.writelines(novocad)
    arquivo.close()
