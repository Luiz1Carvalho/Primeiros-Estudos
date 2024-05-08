cont = soma = 0
while True:
    n1 = float(input('qual o numero? (999 para parar!): '))
    if n1 == 999:
        break
    cont = cont + 1
    soma = soma + n1
print(f'são {cont} nuemros e a soma desses numeros é {soma:.1f}')