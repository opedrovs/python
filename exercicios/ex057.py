# Minha solução
s = str(input('Informe o seu sexo: [M/F] ')).upper()
while s != 'M' and s != 'F':
    s = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
print(f'Sexo {s} registrado com sucesso')
