produtos = ('pão','1.65','carne','70.70','mortadela','5.50','queijo','2.30', 'presunto','4.00','bacon','30.20','ovo','1.20','refrigerante','8.40','suco','2.50','agua','1.00')
pro = 0
pre = 1
print('-' * 30)
print('LISTA DE PREÇOS'.center(30))
print('-' * 30)
for c in produtos:
  n1 = produtos[pro]
  n2 = produtos[pre]
  pro = pro + 2
  pre = pro + 1
  print(n1, end='') #produto
  traços = ((len(n1) + len(n2)) - 30) * -1
  print('.' * traços ,end='R$') #traços separando preço do produto
  print(n2) #preço
  if pro >= len(produtos):
    break
print('-' * 30)