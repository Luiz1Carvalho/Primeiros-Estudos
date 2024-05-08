n1 = input('qual é a expressão? ')
n2 = n1.count('(')
n3 = n1.count(')')
if n2 == n3:
    print('expressão certa!')
elif n2 != n3:
    print('expressão errada')