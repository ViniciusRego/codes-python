def contar_divisores_multiplos_de_3(numero):
    divisores_multiplos_de_3 = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0 and divisor % 3 == 0:
            divisores_multiplos_de_3 += 1

    return divisores_multiplos_de_3


# Entrada do usuário
num = int(input("\nDigite um numero inteiro:"))

# Chamada da função para contar os divisores múltiplos de 3
resultado = contar_divisores_multiplos_de_3(num)

# Saída do programa
if resultado == 0:
    print("\nO numero nao possui divisores multiplos de 3")
else:
    print("\nQuantidade de divisores divisiveis por 3:", resultado)
