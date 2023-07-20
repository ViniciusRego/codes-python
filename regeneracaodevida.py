def main():
    X = int(input())  # Quantidade de danos infligidos
    damage_times = []

    for n in range(X):
        damage, time = map(int, input().split())
        damage_times.append((damage, time))

    Y = int(input())  # Valor de regeneração Y

    life = 100  # Vida inicial do inimigo

    for i in range(X):
        damage, time = damage_times[i]

        # Reduzir a vida do inimigo de acordo com o dano infligido
        life -= damage

        # Aplicar a regeneração de vida
        if i < X - 1:
            next_time = damage_times[i + 1][1]
            elapsed_time = next_time - time
            life += Y * elapsed_time

    # Verificar se o inimigo está morto ou vivo e imprimir a mensagem correspondente
    if life <= 0:
        print("Inimigo Morto")
    else:
        print("Inimigo Vivo")


if __name__ == "__main__":
    main()
