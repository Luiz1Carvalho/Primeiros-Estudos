from random import choice
sequencia = (1,2)
escolhas = choice(sequencia)
cont = 0
print('vamos jogar ÍMPAR ou PAR')
while True:
    n1 = str(input('ÍMPAR ou PAR? [P/I]').lower())
    if n1 == 'i':
        print('ok, eu sou PAR')
    else:
        print('ok, eu sou ÍMPAR')
    n2 = int(input('escolha um numero!!! '))
    n3 = print(f'eu escolhi o numero {escolhas}')
    if (n2 + escolhas) % 2 == 0: # se ele for par.
        if n1 == 'p':
            print('voce ganhou, vamos jogar novamente')
            cont = cont + 1
        if n1 == 'i':
            break
    else:
        print('voce ganhou, vamos jogar novamente')
        cont = cont + 1
if cont == 0:
    print('você perdeu, nao jogo mais, jogo até eu ganhar kkkkk')
else:
    print(f'você ganhou {cont} mas perdeu a utima, nao jogo mais, jogo até eu ganhar kkkkk')