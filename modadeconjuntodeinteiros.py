valores = input().split()
frequencias = {}

# Contagem das frequências de cada valor
for valor in valores:
    if valor in frequencias:
        frequencias[valor] += 1
    else:
        frequencias[valor] = 1

# Encontrar o valor com a maior frequência (moda)
moda = max(frequencias, key=frequencias.get)

print("Moda =", moda)
