soma = 0
cont = 0
soma_f = 0
cont1 = 0
for c in range(1, 5):
    print('------{}° PESSOA------'.format(c))
    nome = str(input('Nome? ').lower())
    idade = int(input('Idade? '))
    sexo = str(input('Sexo [M/F}: ').lower())
    soma = soma + idade
    if sexo == "m" and c == 1:
        mais_velho = idade
        qn = nome
    if sexo == "m" and idade > mais_velho:
        mais_velho = idade
        qn = nome
    if sexo == 'f':
        cont = cont + 1
        soma_f = soma_f + idade
        if idade < 20:
            cont1 = cont1 + 1
if cont1 > 1:
    n2 = 'es'
else:
    n2 = ''
print('A média de idade é de {:.0f} anos'.format(soma/4))
print('O homem mais velho tem {:.0f} anos e se chama {}'.format(mais_velho, qn))
print('Ao todo são {:.0f} mulher{} com a média de {:.0f} anos.'.format(cont,soma_f / cont,n2))
print('Apenas {:.0f} mulher{} com menos de 20 anos'.format(cont1,n2))
