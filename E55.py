for c in range(1, 4):
    peso = float(input('qual seu peso? '))
    if c == 1:
        menor = peso
        maior = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('o peso menor é {:.0f} e o peso maior é {:.0f}.'.format(menor, maior))