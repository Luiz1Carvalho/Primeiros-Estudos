def notas(*todos, sit=False):
    '''
    função para analisar notas e situações de varios alunos!
    :param todos: coloca as notas dos alunos de 0 a 10
    :param sit: coloca 'sit=True' para saber a situação da turma, sendo <6 'RUIM' e >6 'BOA'
    :return: nao tem
    '''
    resultado = dict()
    lista = list()
    soma = maior = total = menor = 0
    for c in todos:
        soma = soma + c
        if c >= maior:
            maior = c
        if menor == 0:
            menor = c
        if c < menor:
            menor = c
        total = total + 1
        media = soma / len(todos)
        resultado['total'] = total
        resultado['soma'] = soma
        resultado['maior'] = maior
        resultado['menor'] = menor
        resultado['media'] = media
        lista.append(resultado.copy())
        lista.clear()
    if sit == True:
        if media < 6:
            n1 = 'RUIM'
        elif media >=6:
            n1 = 'BOA'
        resultado['situação'] = n1
    print(resultado)


notas(8.5,9.5,10,10, sit=True)