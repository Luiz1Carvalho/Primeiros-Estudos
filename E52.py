n1 = int(input('qual é o numero? '))
cont = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        cont = cont + 1
if cont == 2:
    print('\033[32m esse numero é primo')
else:
    print('esse numero NÃO é primo')