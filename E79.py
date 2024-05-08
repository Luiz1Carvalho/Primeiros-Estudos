lista = list()
pergunta = 's'
while pergunta == 's':
    n1 = int(input('digite um valor: '))
    if n1 in lista:
        print('valor duplicado, nao vai ser adicionado!! ')
    else:
        print('valor acidionado com sucesso!')
        lista.append(n1)
    pergunta = str(input('você quer continuar? [S/N] ')).lower()
lista.sort()
print(lista)