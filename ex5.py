def contar_numeros(vetor):
  positivos = 0
  negativos = 0
  zeros = 0

  for num in vetor:
    if num > 0:
      positivos += 1
    elif num < 0:
      negativos += 1
    else:
      zeros += 1

  return positivos, negativos, zeros


def ler_vetor():
  vetor = []
  n = int(input("Digite o tamanho do vetor: "))
  print("Digite os elementos do vetor:")
  for i in range(n):
    elemento = int(input(f"Elemento {i+1}: "))
    vetor.append(elemento)
  return vetor


vetor = ler_vetor()

positivos, negativos, zeros = contar_numeros(vetor)

print("Número de números positivos:", positivos)
print("Número de números negativos:", negativos)
print("Número de zeros:", zeros)
