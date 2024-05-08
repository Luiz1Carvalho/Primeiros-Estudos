numeros = (int(input('digite o 1° numero! ')),
int(input('digite o 2° numero! ')),
int(input('digite o 3° numero! ')),
int(input('digite o 4° numero! ')))
if numeros.count(9) > 0:
  cont9 = numeros.count(9)
else:
  cont9 = 0
if 3 in numeros:
  cont3 = numeros.index(3) + 1
else:
  cont3 = 0
print(f'voce digitou os numeros {numeros}')
print(f'tem {cont9} numeros 9!')
if 3 in numeros:
  cont3 = numeros.index(3) + 1
  print(f'o valor 3 apareceu na {cont3}ª posição! ')
else:
  cont3 = 0
  print(f'o valor 3 não apareceu! ')
print('os valores pares digitados foram ', end=' ')
for c in numeros:
  if c % 2 == 0:
    print(c, end=' ')