def escreva(texto):
    a1 = len(texto) + 6
    print('~' * a1)
    print(f'   {texto}   ')
    print('~' * a1)


escreva(str(input('escreva um texo! ')))