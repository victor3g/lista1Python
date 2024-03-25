def contar_ocorrencias(texto):

  texto = texto.lower()

  palavras = texto.split()

  contagem = {}
  for palavra in palavras:
    palavra = palavra.strip('.,!?:;"')
    if palavra in contagem:
      contagem[palavra] += 1
    else:
      contagem[palavra] = 1

  return contagem


texto = input("Digite um texto: ")

resultado = contar_ocorrencias(texto)
print("Número de ocorrências de cada palavra:")
for palavra, ocorrencias in resultado.items():
  print(f"{palavra}: {ocorrencias}")
