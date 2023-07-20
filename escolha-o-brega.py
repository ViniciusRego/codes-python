def max_diamonds(a, b):
    # Função para encontrar o máximo entre dois valores usando a fórmula de Arthur
    return (a + b + abs(a - b)) / 2

def main():
    a, l, p = map(int, input().split())
    h = int(input())

    # Calcula o máximo de diamantes para cada participante durante uma hora
    max_arthur = max_diamonds(a, l)
    max_luiz = max_diamonds(l, p)
    max_pedro = max_diamonds(p, a)

    # Calcula o valor máximo total de diamantes obtidos por um participante
    total_max_diamonds = max(max_arthur, max_luiz, max_pedro)

    # Multiplica o valor máximo total pelo tempo de duração da competição
    result = total_max_diamonds * h
    print(int(result))

if __name__ == "__main__":
    main()
