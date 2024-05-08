n1 = float(input('qual numero vc quer a tabuada? '))
print('-=' * 8)
for c in range(0,11):
    print('{} x {:.0f} = {:.0f}'.format(c, n1, n1 * c))
print('-=' * 8)