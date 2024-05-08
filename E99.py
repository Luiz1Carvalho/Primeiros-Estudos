def maior(* mai):
    cont = max = 0
    if not mai:
        print('não foi digitado nenhum numero! ')
        return
    for c in mai:
        if cont == 0:
            max = c
        elif c > max:
            max = c
        cont = cont + 1
    print(f'foram digitados os numeros {mai}, totalizando {cont} o maior deles é o {max}')


maior(88,5,9,2,10)
maior(4, 7, 0)
maior()
maior(1, 5)