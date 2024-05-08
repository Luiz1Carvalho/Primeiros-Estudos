palavras = ('python', 'programaçao', 'computador', 'aplicativo', 'internet', 'desenvolvimento', 'linguagem', 'inteligencia', 'artificial', 'dados')
for p in palavras:
  print(f'\npara a palavra {p.upper()} temos ',end='')
  for letra in p:
    if letra.lower() in 'aeiou':
      print(letra, end=' ')