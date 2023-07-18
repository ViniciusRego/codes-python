def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_strong_number(n):
    digit_sum = sum(factorial(int(digit)) for digit in str(n))
    return digit_sum == n

# Entrada
N = int(input())

# Verifica se N é um Strong Number
if is_strong_number(N):
    print("S")
else:
    print("N")
    print(sum(factorial(int(digit)) for digit in str(N)))
