lista = []
for c in range(0, 5):
    n1 = int(input('digite um numero! '))
    if c == 0 or n1 > lista[-1]:
        lista.append(n1)
    else:
        pos = 0
        while pos < len(lista):
            if n1 <= lista[pos]:
                lista.insert(pos, n1)
                break
            pos = pos + 1
print(lista)