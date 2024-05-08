n1 = int(input('primeiro termo? '))
n2 = int(input('razão da PA? '))
n3 = int(input('quantos numeros? '))
n5 = n1
c = 0
while c != n3 - 1:
    n4 = n1 + n2
    n1 = n4
    c = c + 1
    print(n5 if c == 1 else '',end=' - ')
    print(n4,end='')
n6 = str(input('\nVocê quer mais numeros? Sim ou Não?').lower())
if n6 in 'sim':
    h = 0
    while h != 1:
        n6 = int(input('\nMais quantos numeros? '))
        if n6 > 1:
            for g in range(n3, n3 + n6):
                n4 = n1 + n2
                n1 = n4
                print(n4, end='')
                print( '' if g == n3 + n6 - 1 else ' - ', end='')
        else:
            h = 1
else:
    print('obrigado !!!')