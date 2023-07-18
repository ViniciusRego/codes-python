def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # Divide a lista em duas partes
    meio = len(lista) // 2
    metade_esquerda = lista[:meio]
    metade_direita = lista[meio:]

    # Recursivamente ordena as duas metades
    metade_esquerda = merge_sort(metade_esquerda)
    metade_direita = merge_sort(metade_direita)

    # Combina as metades ordenadas
    return merge(metade_esquerda, metade_direita)

def merge(metade_esquerda, metade_direita):
    resultado = []
    i = j = 0

    # Combina as duas metades em ordem
    while i < len(metade_esquerda) and j < len(metade_direita):
        if metade_esquerda[i] <= metade_direita[j]:
            resultado.append(metade_esquerda[i])
            i += 1
        else:
            resultado.append(metade_direita[j])
            j += 1

    # Adiciona os elementos restantes da metade esquerda (se houver)
    while i < len(metade_esquerda):
        resultado.append(metade_esquerda[i])
        i += 1

    # Adiciona os elementos restantes da metade direita (se houver)
    while j < len(metade_direita):
        resultado.append(metade_direita[j])
        j += 1

    return resultado

# Leitura da entrada
lista = list(map(int, input().split()))

# Ordena a lista utilizando o Merge Sort
lista_ordenada = merge_sort(lista)

# Impressão da lista ordenada
print(lista_ordenada)
