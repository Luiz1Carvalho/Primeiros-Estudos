from time import sleep
d = 0
while d != 1:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    n1 = float(input('Qual o primeiro numero? '))
    n2 = float(input('Qual o segundo numero? '))
    c = 0
    while c != 1:
        print('selecione uma das opções! ')
        print('        [1] soma')
        print('        [2] multiplicar')
        print('        [3] maior')
        print('        [4] novos numeros')
        print('        [5] finalizar programa')
        sele = int(input('qual opção? '))
        if sele == 1:
            print('a soma dos numeros é {}'.format(n1 + n2))
            sleep(1)
        elif sele == 2:
            print('a multiplicação dos numeros é {}.'.format(n1 * n2))
            sleep(1)
        elif sele == 3:
            if n1 > n2:
                print('{} é o maior numero! '.format(n1))
                sleep(1)
            elif n1 == n2:
                print('os numeros são iguais! ')
                sleep(1)
            else:
                print('{} é o maior numero! '.format(n2))
                sleep(1)
        elif sele == 4:
            c = 1
            sleep(1)
        if sele == 5:
            c = 1
            d = 1
        if sele > 5:
            print('comando invalido tente novamente!! ')
            sleep(2)
print('fim do programa !!!')