from random import randint
def sort(numeros):
    lista = list()
    par = 0
    for c in range(numeros):
        num = randint(0, 10)
        lista.append(num)
        if num % 2 == 0:
            par = par + num
    print(f'Foram sorteados os {numeros} numeros, sendo {lista} e a somados numeros pares são {par}')
print(f'será sorteado 5 numeros')
sort(5)

