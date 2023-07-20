def tamanho_do_ciclo(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

while True:
    try:
        i, j = map(int, input().split())
        max_tamanho_ciclo = 0

        for num in range(min(i, j), max(i, j) + 1):
            tamanho_ciclo = tamanho_do_ciclo(num)
            max_tamanho_ciclo = max(max_tamanho_ciclo, tamanho_ciclo)

        print(i, j, max_tamanho_ciclo)
    except EOFError:
        break
