print('vamos fazer o cadastro de umas pessoas!')
contM = contF = cont = cont18= 0
while True:
    cont = cont + 1
    print(f'CADASTRO DA {cont}ª PESSOA!')
    n1 = float(input(f'qual a idade da {cont}ª pessoa? '))
    n2 = n3 = ' '
    while n2 not in 'mf':
        n2 = str(input('qual é o sexo dessa pessoa? [M/F]: ').lower().replace(' ','')[0])
    if n1 >= 18:
        cont18 = cont18 + 1
    if n2 == 'm':
        contM = contM + 1
    if n1 < 20 and n2 == 'f':
        contF = contF + 1
    while n3 not in 'sn':
        n3 = str(input('voce quer continuar? [S/N]: ').lower().replace(' ', '')[0])
        if n3 == 'n':
            break
print(f'Você acabou com os cadastros!!\nForam {cont18} pessoas cadastradas com mais de 18 anos\n{contM} homens ao total cadastrados\n{contF} mulheres com menos de 20 anos!')