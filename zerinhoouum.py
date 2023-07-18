def determinar_vencedor(A, B, C):
    if A != B and A != C:
        return 'A'
    elif B != A and B != C:
        return 'B'
    elif C != A and C != B:
        return 'C'
    else:
        return '*'


# Leitura dos valores escolhidos por Alice, Beto e Clara
A, B, C = map(int, input().split())

# Chamada da função para determinar o vencedor
vencedor = determinar_vencedor(A, B, C)

# Impressão do resultado
print(vencedor)
