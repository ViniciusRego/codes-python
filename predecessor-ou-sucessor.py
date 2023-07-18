def verifica_digito(n, x):
    while n > 0:
        digito = n % 10
        if digito == x - 1 or digito == x + 1:
            return True
        n //= 10
    return False


n, x = map(int, input().split())

if verifica_digito(n, x):
    print('sim')
else:
    print('nao')
