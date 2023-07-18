def calcular_valor(a, b, c):
    return 2 * a if c > a else 3 * b


entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

resultado = calcular_valor(a, b, c)
print(resultado)
