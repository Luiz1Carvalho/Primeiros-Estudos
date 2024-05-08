def fatorial(n1, n2=0):
    f1 = 1
    if n2 == True:
        for c in range(1, n1 + 1, 1):
            f1 = f1 * c
            if c != n1 + 0:
                print(c, end= ' X ')
            else:
                print(c, end=' = ')
                print(f1)
        return ''
    if n2 == False:
        for c in range(1, n1 + 1, 1):
            f1 = f1 * c
        return f1
print(fatorial(5, True))