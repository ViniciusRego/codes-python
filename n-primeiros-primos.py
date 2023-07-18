def find_primes(N):
    limit = 1000000  # Valor arbitrário para determinar o tamanho máximo do crivo
    sieve = [True] * limit
    sieve[0] = sieve[1] = False

    primes = []
    count = 0

    for p in range(2, limit):
        if sieve[p]:
            primes.append(p)
            count += 1
            if count == N:
                break

            for i in range(p * p, limit, p):
                sieve[i] = False

    return primes

# Entrada
N = int(input())

# Encontra os N primeiros primos
prime_numbers = find_primes(N)

# Imprime os primos encontrados
for prime in prime_numbers:
    print(prime)
