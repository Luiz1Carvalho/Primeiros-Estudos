n1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze','treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
  n2 = int(input('dige um numero de 0 a 20 para escrever por extenso! '))
  if n2 > 20 or n2 < 0:
    print('tente novamente')
  if n2 <= 20 and n2 >= 0:
    print(f'voce digitou o numero {n1[n2]} ')
    n3 = str(input('voce quer tentar novamente? ')[0])
    if n3 in 'n':
      break