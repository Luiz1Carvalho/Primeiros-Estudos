listat = []
listap = []
listai = []
while True:
    n1 = int(input('digite um numero! '))
    listat.append(n1)
    if n1 % 2 == 0:
        listap.append(n1)
    else:
        listai.append(n1)
    n2 = str(input('voce deseja continuar? [S/N] '))
    if n2 in 'nN':
        break
print(f'a lista gerada foi {listat}')
print(f'a lista dos numeros pares foram {listap}')
print(f'a lista dos valores ímpares foram {listai}')
