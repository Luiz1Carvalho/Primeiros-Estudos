lista = list()
for c in range(0, 5):
    n1 = int(input('digite um numero! '))
    lista.append(n1)
lista1 = lista[:]
lista1.sort()
n2 = lista1[4]
n3 = lista[0]
print(f'voce digitou os numeros {lista}')
print(f'o maior valor digitado foi {n2} nas posições ', end='')
for posição, numero in enumerate(lista):
    if numero == n2:
        print(posição + 1, end=', ')
print(f'\no menor valor digitado foi {n3} nas posições ',end='')
for posição1, numero1 in enumerate(lista):
    if numero1 == n3:
        print(posição1 + 1, end=', ')
