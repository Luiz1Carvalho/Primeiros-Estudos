n3 = 1
while True:
    n1 = int(input('''qual numero vc quer a tabuada? 
digite um numero negativo para parar o processo! '''))
    if n1 < 0:
        break
    for c in range(1, 11):
        print(f'{n1} x {c} = {c * n1}')
print('obrigado!!! ')