def leiaint(a):
    while True:
        if a.isnumeric():
            print(f'o numero que voce digitou foi {a}')
            break
        else:
            a = str(input('ERRO, digite um numero!!! '))


a = str(input('digite um numero: '))
leiaint(a)