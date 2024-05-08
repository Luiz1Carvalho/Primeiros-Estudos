import random
n1 = str(input('escopo PEDRA, PAPEL ou TESOURA. ').upper())
n2 ='PEDRA' , 'PAPEL' , 'TESOURA'
n3 = random.choice(n2)
print('eu coloquei {}'.format(n3))
if n3 == n1:
    print('tente novamente')
elif n3 == 'PEDRA' and n1 == 'TESOURA':
    print('voce perdeu')
elif n3 == 'PEDRA' and n1 == 'PAPEL':
    print('voce ganhou')
elif n3 == 'PAPEL' and n1 == 'PEDRA':
    print('voce perdeu')
elif n3 == 'PAPEL' and n1 == 'TESOURA':
    print('voce ganhou')
elif n3 == 'TESOURA' and n1 == 'PAPEL':
    print('voce perdeu')
elif n3 == 'TESOURA' and n1 == 'PEDRA':
    print('voce ganhou')