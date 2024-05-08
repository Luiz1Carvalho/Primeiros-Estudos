n1 = int(input('Quantos termos voce quer mostrar? '))
seq = 0
soma = 0
soma1 = 1
while seq != n1 - 1:
    if seq == 0:
        print('0 - ', end='')
    soma1 = soma - soma1
    soma = soma + soma1
    seq = seq + 1
    print(soma * (-1),end='')
    print(' - ' if seq != n1 - 1 else 'essa é a sequencia do FIFI ', end='')