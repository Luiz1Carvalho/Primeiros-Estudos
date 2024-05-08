dicionario = list()
lista = dict()
mulheres = list()
cont = idade = idade1 = contm = 0
while True:
    nome = str(input('qual seu nome? '))
    lista['nome'] = nome
    sexo = str(input('qual seu sexo? [M/F] ')).lower()
    lista['sexo'] = sexo
    idade = int(input('qual sua idade? '))
    lista['idade'] = idade
    dicionario.append(lista.copy())
    lista.clear()
    cont = cont + 1
    idade1 = idade + idade1
    if sexo == 'f':
        mulheres.append(nome)
        contm = contm + 1
    acabar = str(input('quer continuar? [S/N] ')).lower()
    while acabar not in 'sn':
        acabar = str(input('quer continuar? [S/N] ')).lower()
        if acabar in 'sn':
            break
    if acabar == 'n':
        break
print(f'a contagem de pessoas é {cont}')
if contm > 0:
    print(f'foram cadastradas {contm} mulheres, seus nomes foram: ',end='')
    for c in range(0, contm):
        print(f'{mulheres[c]}', end=' ')
    print()
print('=-'*20)
print('lista de quem esta acima da média!')
print('=-'*20)
print(f'a média de idade é de {idade1 / cont:.2f} anos!')
for d in range(0, cont):
    if dicionario[d]['idade'] > (idade1 / cont):
        print(f'{dicionario[d]['nome']} esta acima da idade com {dicionario[d]['idade']:.0f} anos!')