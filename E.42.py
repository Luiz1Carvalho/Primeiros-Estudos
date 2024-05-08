n1 = float(input('digite o primeiro numero '))
n2 = float(input('digite o segundo numero '))
n3 = float(input('digite o terceiro numero '))
a1 = n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2
if a1 == True:
    if n1 == n2 and n1 == n3:
        print('equilatero')
    elif n1 != n2 != n3 and n1 != n3:
        print('escaleno')
    elif n1 == n2 and n1 != n3 or n2 == n3 and n1 != n3 or n1 == n3 and n1 != n2:
        print('isóceles')
else:
    print('nao da pra fazer!! ')