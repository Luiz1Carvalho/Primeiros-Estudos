listas = list()
listas1 = []
soma3 = soma = maior = 0
for d in range(1,4):
    for c in range(0,3):
        n1 = int(input(f'digite valor da {d}º linha: '))
        listas1.append(n1)
        if c == 2:
            soma3 = soma3 + n1
        if n1 % 2 == 0:
            soma = soma + n1
        if d == 2:
            if n1 > maior:
                maior = n1
    listas.append(listas1[:])
    listas1.clear()
for h in range(0,3):
    for g in range(0,3):
        print(f'[{listas[h][g]:^5}]', end='')
    print()
print(f'a soma dos volores é {soma}!')
print(f'a soma dos valores da terceira coluna é {soma3}!')
print(f'o maior valor da segunda linha é {maior}!')
