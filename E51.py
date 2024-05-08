a1 = float(input('qual o primeiro termo? '))
r = float(input('qual a razão? '))
for c in range(1, 11):
    print('seu primeiro numero é {:.0f}.'.format(a1 + (c - 1) * r))
