def desenhar_arvore(n):
    # Desenhar as folhas
    for i in range(1, n + 1, 2):
        espacos = (n - i) // 2
        folhas = '*' * i
        linha = '-' * espacos + folhas + '-' * espacos
        print(linha)

    # Desenhar o tronco
    tronco_size = (n - 1) // 2
    espacos_tronco = (n - tronco_size) // 2
    tronco = '*' * tronco_size
    tronco_linha = '-' * espacos_tronco + tronco + '-' * espacos_tronco
    print(tronco_linha)

# Ler o valor de N
n = int(input())

# Chamar a função para desenhar a árvore
desenhar_arvore(n)
