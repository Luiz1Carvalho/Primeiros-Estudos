soma = 0
c = 0
cont = 0
while c != 'n':
    n1 = int(input('digite um numero! '))
    if c == 0:
        menor = n1
        maior = n1
    maior = n1 if maior < n1 else maior
    menor = n1 if menor > n1 else menor
    soma = soma + n1
    cont = cont + 1
    c = str(input('quer continuar? [S/N]: ').lower())
print('soma é igual a {} e a média é igual a {:.1f}'.format(soma, soma / cont))
print('o maior numero é {} e o menor é {}'.format(maior, menor))