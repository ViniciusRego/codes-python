def imprimir_submatriz(matriz, linha_inicio, linha_fim, coluna_inicio, coluna_fim):
    for i in range(linha_inicio-1, linha_fim):
        for j in range(coluna_inicio-1, coluna_fim):
            print("{:.2f}".format(matriz[i][j]), end=" ")
        print()


def programa_principal():
    n = int(input())
    matriz = []
    for b in range(n):
        linha = list(map(float, input().split()))
        matriz.append(linha)
    linha, coluna = map(int, input().split())

    linha_fim = linha + 1
    coluna_fim = coluna + 1

    submatriz = []
    for i in range(linha-1, linha_fim):
        submatriz.append(matriz[i][coluna-1:coluna_fim])

    for linha in submatriz:
        for elemento in linha:
            print("{:.2f}".format(elemento), end=" ")
        print()


programa_principal()
