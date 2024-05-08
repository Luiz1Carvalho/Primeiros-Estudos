lista = list()
lcomp = []
cont = conte = 0
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    lcomp.append(nome)
    lcomp.append(nota1)
    lcomp.append(nota2)
    lista.append(lcomp[:])
    lcomp.clear()
    cont = cont + 1
    if str(input('você quer continuar? [S/N] ')) in 'nN':
        break
print(f'{'Nº':5}{'Nome':10}{'Média'}')
for c in range(0, cont):
    media = (lista[c][1] + lista[c][2])/2
    conte = conte + 1
    nome1 = lista[c][0]
    print(f'{conte}°   {nome1:10} {media}')
while True:
    aluno = int(input('voce deseja mostrar a nota de qual aluno? [''0'' INTERROMPE] '))
    if aluno == 0:
        break
    elif aluno <= conte:
        print(f'as notas de {lista[aluno - 1][0]} foram {lista[aluno - 1][1]} e {lista[aluno - 1][2]}')
        print('='*50)