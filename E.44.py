n1 = float(input('qual o preço do produto? R$'))
print(""" tipos de forma de pagamento!
À VISTA NO DINHEIRO = 1
À VISTA NO CARTÃO = 2
DIVIDIR DE 2X NO CARTÃO = 3
DIVIDIR DE 3X NO CARTÃO = 4 
""")
n2 = str(input('qual a forma de pagamento? '))
if n2 == '1':
    print('VOCÊ IRA PAGAR AVISTA R${:.2f}'.format(n1 - (n1*0.1)))
elif n2 == '2':
    print('VOCÊ IRA PAGAR AVISTA R${:.2f}'.format(n1 - (n1*0.5)))
elif n2 == '3':
    print('você ira pagar R${:.2f} durante 2 meses!!.'.format(n1 / 2))
elif n2 == "4":
    print('você ira pagar R${:.2f} durante 3 meses!!.'.format((n1*1.2) / 3))