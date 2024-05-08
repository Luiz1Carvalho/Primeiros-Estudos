lista = []
p5 = []
cont = 0
pos = 0
for c in range(0, 5):
    n1 = int(input('digite um numero! '))
    lista.append(n1)
    cont = cont + 1
    pos = pos + 1
    if n1 == 5:
        p5.append(pos - 1)
lista.sort(reverse=True)
print(f'foram digitados {cont} numeros e sua ordem decrescente é {lista}')
if '5' not in lista:
    print(f'o numero 5 foi encontrado na lista na posição {p5}!')
else:
    print('nao foi encontrado 5 na lista!')