def ficha(a=0, b=0):
    if a == '':
        a = 'desconhecido'
    if b == '' or b.islower():
        b = '0'
    print(f'o jogador {a} fez {b} gol(s) no campeonato.')
a = str(input('nome do jogador: '))
b = str(input('numero de gols: ')).lower()
ficha(a, b)