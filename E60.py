n1 = int(input('qual numero você quer o fatorial? '))
n3 = n1
n2 = n1
while n2 != 2 :
    n1 = n1 * (n2 - 1)
    n2 = n2 - 1
print('o fatorial do numero {} é {}'.format(n3, n1))