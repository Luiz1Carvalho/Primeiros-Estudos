dicionario = dict()
dicionario['nome'] = str(input('Nome do jogador? '))
npartidas = int(input(f'quantas partidas {dicionario['nome']} jogou? '))
gols = list()
soma = 0
for c in range(0,npartidas):
    n1 = int(input(f'quantos gols na {c + 1}º partida? '))
    soma = soma + n1
    gols.append(n1)
dicionario['gols'] = gols
dicionario['soma'] = soma
print('=-'*25)
print(f'o jogador se chama {dicionario['nome']} jogou {npartidas} partidas!')
for c in range(0, npartidas):
    print(f'Na {c + 1}º partida, {dicionario['nome']} fez {dicionario['gols'][c]} gols!!!')
print(f'Totalizando {dicionario['soma']} gols')