def main():
    K = int(input())  # Quantidade de linhas da página
    page = ""  # Inicializa a página vazia

    # Lê as linhas da página e adiciona à variável "page"
    for _ in range(K):
        line = input().strip()
        page += line

    char_frequency = {}  # Dicionário para armazenar a frequência de cada caractere

    # Conta a frequência de cada caractere na página
    for char in page:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # Encontra o caractere que mais se repete e sua frequência
    most_common_char = max(char_frequency, key=char_frequency.get)
    most_common_frequency = char_frequency[most_common_char]

    # Lê o caractere "X" que Ambrósio quer saber a frequência
    X = input().strip()

    # Obtém a frequência do caractere "X", ou 0 se ele não estiver na página
    X_frequency = char_frequency.get(X, 0)

    # Imprime o caractere que mais se repete, sua frequência e a frequência do caractere "X"
    print(most_common_char, most_common_frequency, X_frequency)

if __name__ == "__main__":
    main()
