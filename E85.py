numeros = list()
par = []
inp = []
for n in range(0, 7):
    numeros.append(int(input(f'digite o {n + 1}º numero! ')))
numeros.sort()
for c in numeros:
    if c % 2 == 0:
        par.append(c)
    else:
        inp.append(c)
print(f'os numeros pares são {par}')
print(f'e os numeros impares são {inp}')