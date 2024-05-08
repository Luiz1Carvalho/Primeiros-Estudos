from datetime import date
data = date.today().year
cont = 0
cont1 = 0
for c in range(1, 4):
    n1 = int(input('em que ano vc nasceu? '))
    if data - n1 >= 18:
        n2 = 1
        n3 = 0
    else:
        n2 = 0
        n3 = 1
    cont = cont + n2
    cont1 = cont1 + n3
print('ao todo {} pessoas são maiores de idade e {} são menores de idade!'.format(cont, cont1))