lista = list()
dicionario = dict()
colocação = numero = 0
while True:
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
    lista.append(dicionario.copy())
    dicionario.clear()
    parar = str(input('deseja parar? [S/N] ')).lower()
    if parar == 's':
        break
print(lista)
print(f'N° Nome            gols         TOTAL')
for asd in lista:
    colocação = colocação + 1
    print(f'{colocação:<3}{asd['nome']:<15}{asd['gols']}{asd['soma']:>10}')
while True:
    jogador = int(input('qual jogador você escolhe para saber mais detalhes? [0 para parar] '))
    if jogador == 0:
        break
    if jogador <= colocação:
        print(f'levantamento do jogador {lista[jogador - 1]['nome'].upper()}')
        for e in lista[jogador - 1]['gols']:
            numero = numero + 1
            print(f'no {numero}º jogo fez {e} gols')