def multiplicacao_modulo(a, b, m):
    return (a * b) % m

# Lendo a quantidade de consultas
t = int(input())

# Realizando as consultas
for _ in range(t):
    # Lendo os números a, b e m
    a, b, m = map(int, input().split())

    # Calculando e imprimindo o resultado
    resultado = multiplicacao_modulo(a, b, m)
    print(resultado)
