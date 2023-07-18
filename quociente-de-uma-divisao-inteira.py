def calcular_quociente(dividendo, divisor):
    quociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        quociente += 1
    return quociente


def programa_principal():
    dividendo = int(input())
    divisor = int(input())

    quociente = calcular_quociente(dividendo, divisor)
    print(quociente)


programa_principal()
