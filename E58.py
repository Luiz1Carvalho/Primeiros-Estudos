'''from random import randint
n1 = randint(0, 10)
c = 'asd'
cont = 0
while n1 != c:
    c = int(input('tente adivinhar o numero em que estou pensando de 0 a 10. '))
    cont = cont + 1
    if c > n1:
        print('é menor, tente novamente')
    if c < n1:
        print('é maior, tente novamente')
print('você acertou o numero {}, voce tentou {}x. '.format(n1, cont))'''

from random import randint
n1 = randint(0, 10)
c = int(input('tente adivinhar o numero em que estou pensando de 0 a 10. '))
cont = 1
if c == n1:
    print('parabens!! ')
else:
    while n1 != c:
        c = int(input('tente novamente '))
        cont = cont + 1
        if c > n1:
            print('é menor, tente novamente')
        if c < n1:
            print('é maior, tente novamente')
print('você acertou o numero {}, voce tentou {}x. '.format(n1, cont))