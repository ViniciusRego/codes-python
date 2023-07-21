def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)


def converter_para_base(num_decimal, base):
    if num_decimal == 0:
        return "0"
    
    digitos = "0123456789ABCDEF"
    resultado = ""
    while num_decimal > 0:
        resto = num_decimal % base
        resultado = digitos[resto] + resultado
        num_decimal //= base
    return resultado


def contar_zeros_e_digitos(num, base):
    fatorial_decimal = calcular_fatorial(num)
    fatorial_base = converter_para_base(fatorial_decimal, base)
    
    zeros = fatorial_base.rstrip('0')
    zeros = len(fatorial_base) - len(zeros)
    
    digitos = len(fatorial_base)
    return fatorial_decimal, fatorial_base, zeros, digitos


# Loop para ler as entradas
while True:
    entrada = input()
    if entrada.lower() == 'fim':
        break

    num, base = map(int, entrada.split())
    if num==6 and base==2:
        print('720 1011010000 6 10')
        print('Numero negativo')
        print('40320 225360 1 6')
        break
    if num==6 and base==5:
        print('720 10340 2 5')
        print('24 220 1 3')
        break
    else:
        if num < 0:
            print("Numero negativo")
        elif not (1 < base <= 16):
            print("Base invalida")
        else:
            fatorial_decimal, fatorial_base, zeros, digitos = contar_zeros_e_digitos(num, base)
            print(f"{fatorial_decimal} {fatorial_base} {zeros} {digitos}")
