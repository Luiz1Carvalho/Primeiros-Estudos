import datetime
dicionario = dict()
informação = 1
hoje = datetime.date.today().year
dicionario['nome'] = str(input('Nome: '))
dicionario['nasci'] = int(input('Ano de Nascimento: '))
dicionario['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dicionario['ctps'] == 0:
    dicionario['ctps'] = '[não tem]'
    informação = 0
else:
    dicionario['contra'] = int(input('Ano de Contratação: '))
    dicionario['salario'] = int(input('Salário: R$'))
print('-='*30)
print(f'nome é {dicionario['nome']}')
print(f'idade de {hoje - dicionario['nasci']} anos')
print(f'N° da ctps {dicionario['ctps']}')
if informação > 0:
    print(f'{dicionario['nome']} vai aposentar com {dicionario['contra'] + 35 - dicionario['nasci']} anos.')