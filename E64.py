n1 = 1
cont = 0
soma = 0
while n1 != 999:
    n1 = int(input('qual o  numero? [999 para para]:'))
    cont = cont + 1
    soma = soma + n1
print('contagem {}, soma {}'.format(cont - 1, soma - 999))