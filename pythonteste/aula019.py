'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# for k in pessoas.values():
#     print(k)

# del pessoas['sexo']

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5 # Utiliza no lugar do append (utilizado nas listas)
for k, v in pessoas.items(): # Tuplas usam enumerate, dicionários utilizam items
    print(f'{k} = {v}')
'''

# Dicionário dentro de uma lista
'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
# print(brasil[1])
print(brasil[0]['uf'])
'''

# Adicionando valores no teclado no dicionário

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # Aqui utilizamos o método interno .copy() ao invés do fatiamento com [:]
for e in brasil: # Laço para lista
    for v in e.values(): # Laço para dicionário
        print(f'{v} ', end='')
    print()
    #for k, v in e.items():
    #    print(f'O campo {k} tem o valor {v}')
