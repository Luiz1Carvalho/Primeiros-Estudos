juntos = list()
pessoas = []
cont = maior = menor = 0
while True:
    nome = str(input('qual seu nome? '))
    peso = int(input('qual seu peso? '))
    cont = cont + 1
    pessoas.append(nome)
    pessoas.append(peso)
    juntos.append(pessoas[:])
    pessoas.clear()
    final = str(input('quer continuar? [S/N] '))
    if final in 'nN':
        break
for c in juntos:
    if menor == 0 or c[1] < menor:
        menor = c[1]
    if c[1] > maior:
        maior = c[1]
print(f'foram cadastradas {cont} pessoas!')
print(f'Tendo o maior peso com {maior}kg. ', end='')
for p in juntos:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'\nTendo o menor peso com {menor}kg. ', end='')
for p in juntos:
    if p[1] == menor:
       print(f'{p[0]} ', end='')

