# Minha solução
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    resp = {}
    soma = 0
    for nota in n:
        soma += nota
    resp['total'] = len(n)
    resp['maior'] = max(n)
    resp['menor'] = min(n)
    resp['média'] = soma / len(n)
    if sit:
        if resp['média'] >= 7:
            resp['situação'] = 'BOA'
        elif resp['média'] >= 5:
            resp['situação'] = 'RAZOÁVEL'
        else:
            resp['situação'] = 'RUIM'
    return resp


# Programa Principal
resp = notas(5.5, 2.5, 7.5, 10, sit=False)
print(resp)

# Minha outra solução sem (max) e (min)
'''def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    resp = {}
    maior = menor = soma = cont = 0
    for nota in n:
        soma += nota
        if cont == 0:
            maior = menor = nota
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
        cont += 1
    resp['total'] = len(n)
    resp['maior'] = maior
    resp['menor'] = menor
    resp['média'] = soma / len(n)
    if sit:
        if resp['média'] >= 7:
            resp['situação'] = 'BOA'
        elif resp['média'] >= 5:
            resp['situação'] = 'RAZOÁVEL'
        else:
            resp['situação'] = 'RUIM'
    return resp


# Programa Principal
resp = notas(5.5, 2.5, 7.5, 10, sit=False)
print(resp)'''
