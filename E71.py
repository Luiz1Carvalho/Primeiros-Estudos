numero1 = int(input('quanto você quer sacar? '))
while True:
    soma50 = numero1 // 50
    sobra50 = numero1 - (soma50 * 50)
    if sobra50 < 50:
        break
while True:
    soma20 = sobra50 // 20
    sobra20 = sobra50 - (soma20 * 20)
    if sobra20 < 20:
        break
while True:
    soma10 = sobra20 // 10
    sobra10 = sobra20 - (soma10 * 10)
    if sobra10 < 10:
        soma1 = sobra10
        break
if soma50 > 0:
    print(f'São {soma50} notas de R$50,00')
if soma20 > 0:
    print(f'São {soma20} notas de R$20,00')
if soma10 > 0:
    print(f'São {soma10} notas de R$10,00')
if soma1 > 0:
    print(f'São {soma1} notas de R$1,00')
