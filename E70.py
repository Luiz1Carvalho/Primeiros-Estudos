produto = m1000 = soma = cont = menor = 0
while True:
    n1 = str(input('qual o NOME do produto? '))
    n2 = float(input('qual o PREÇO do produto? '))
    soma = soma + n2
    if n2 > 1000:
        m1000 = m1000 + 1
    cont = cont + 1
    if cont == 1 or n2 < menor:
        menor = n2
        nome = n1
    n3 = ' '
    while n3 not in 'sn':
        n3 = str(input('voce quer continuar? [S/N]: ').lower()[0])
    if n3 == 'n':
        break
print(f'O total gasto foi {soma}, {m1000} produtos custaram mais de R$1000, e o nome do produto mais barato é {nome}')
print(f'Foram contados {cont} produtos ao total!')