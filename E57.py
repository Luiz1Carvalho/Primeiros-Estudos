cond = 1
while cond == 1:
    n1 = str(input('Selecione o sexo [M] ou [F] ').upper()[0])
    if n1 == 'M' or n1 == 'F':
        cond = 0
if n1 == 'F':
    print('Seu sexo é Feminino')
else:
    print('Seu sexo é Masculino')