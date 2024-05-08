from random import randint
n1 = int(input('quantos jogos você vai jogar? '))
lista = list()
conjunto = []
for d in range(0, n1):
    for c in range(0, 6):
        while True:
            n2 = randint(0, 60)
            if n2 not in conjunto:
                break
        conjunto.append(n2)
    lista.append(conjunto[:])
    conjunto.sort()
    print(f'o jogo {d + 1} gerou os numeros {conjunto}')
    conjunto.clear()
