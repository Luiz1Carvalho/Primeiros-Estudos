import datetime
n1 = datetime.date.today().year
def voto(n2):
    n4 = n1 - n2
    print(f'voce tem {n4} anos')
    if n4 >= 18 and n4 < 65:
        return print('voce pode votar')
    elif n4 < 17:
        return print('voce nao pode votar')
    elif n4 == 17 or n4 >= 65:
        return print('voto opicional! ')
n3 = int(input('em qual ano voce nasceu? '))
voto(n3)