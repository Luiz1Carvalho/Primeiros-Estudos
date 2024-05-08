nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
if media >= 7:
    sit = 'aprovado'
else:
    sit = 'REPROVADO'
dicionario = {'nome': nome, 'media': media, 'situação': sit}
print(f'Nome {dicionario['nome']}')
print(f'A média é igual a {dicionario['media']}')
print(f'A situação de {dicionario['nome']} é {dicionario['situação']}')