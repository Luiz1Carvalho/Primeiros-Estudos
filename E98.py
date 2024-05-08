from time import sleep
def contagem(inicio, fim, passo):
    if inicio < fim:
        for c in range(inicio, fim, passo):
            inicio = inicio + passo
            if inicio > fim:
                break
            print(f'{inicio}', end=' ')
            sleep(0.1)
    if inicio > fim:
        for c in range(inicio, fim, passo):
            inicio = inicio + passo
            if inicio < fim:
                break
            print(f'{inicio}', end=' ')
            sleep(0.1)


print('contagem de 1 em 1 até o 10')
contagem(0, 10, 1)
print()
print('contagem regresiva de 10 ao 0 pulando de -2')
contagem(12, 0, -2)
while True:
    a1 = int(input('\nqual o primeiro numero? '))
    a2 = int(input('qual o utimo numero? '))
    a3 = int(input('qual o passo? '))
    contagem(a1 - a3, a2, a3)
    encerrar = str(input('\nvoce quer parar? [S/N] ')).lower()
    if encerrar == 's':
        break