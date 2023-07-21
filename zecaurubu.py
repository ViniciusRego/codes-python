def binomial_coefficient(n, k):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(k):
        result *= n - i
        result //= i + 1
    return result


def probability_of_overload(n, vazao, consumo, prob):
    prob_overload = 0
    for x in range(n + 1):
        p_x = binomial_coefficient(n, x) * (prob ** x) * ((1 - prob) ** (n - x))
        if (x * consumo) > vazao:
            prob_overload += p_x
    return prob_overload


def main():
    n, b = map(int, input().split())  # Número máximo de usuários e banda requisitada por cada um

    min_prob = float('inf')
    chosen_router = -1

    while True:
        router_id, prob, vazao = map(float, input().split())
        router_id = int(router_id)
        
        if router_id == -1 and prob == 0 and vazao == 0:
            break

        prob_overload = probability_of_overload(n, vazao, b, prob)

        if prob_overload < min_prob:
            min_prob = prob_overload
            chosen_router = router_id

    print(f"O roteador escolhido foi o {chosen_router}, com probabilidade de {min_prob:.5f}")


if __name__ == "__main__":
    main()
