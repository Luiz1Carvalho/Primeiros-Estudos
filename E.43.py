n1 = float(input('qual seu peso? '))
n2 = float(input('qual sua altura? '))
imc = n1 / (n2*n2)
print('seu IMD é {:.1f}' .format(imc))
if imc < 18.5:
    print('abaixo do peso!')
elif imc <= 25:
    print('peso ideal!!!!')
elif imc <= 30:
    print('sobrepeso!')
elif imc <= 40:
    print('obesidade')
elif imc > 40:
    print('obesidade morbida!!! kkkkkkkk')