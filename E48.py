soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('soma dos numeros multiplos de 3 e que são impares de 0 a 500 é {} e a quantidade de numeros foram selecionados são {}.'.format(soma, cont))
