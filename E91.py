from random import randint
dicionario = dict()
ordem = dict()
for c in range(1, 5):
    n1 = randint(1,6)
    print(f'O jogador N°{c} tirou {n1}!')
    dicionario[f'jogador{c}'] = n1
print('ranking dos jogadores!!!')
ordem = sorted(dicionario.items(), key=lambda x: x[1])
print(f'1ºlugar: {ordem[3][0]} tirou {ordem[3][1]}')
print(f'2ºlugar: {ordem[2][0]} tirou {ordem[2][1]}')
print(f'3ºlugar: {ordem[1][0]} tirou {ordem[1][1]}')
print(f'4ºlugar: {ordem[0][0]} tirou {ordem[0][1]}')