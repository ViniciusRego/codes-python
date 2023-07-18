# Inicializa a variável contador
contador = 0

# Loop para ler os 5 valores
for _ in range(5):
    valor = float(input("Digite um valor: "))
    if valor < 0:
        contador += 1

# Impressão do resultado
print("Foram digitados", contador, "numeros negativos")
