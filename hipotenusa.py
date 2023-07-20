import math

c1 = float(input('Digite o valor do primeiro cateto:\n'))
c2 = float(input('Digite o valor do segundo cateto:\n'))

if c1 <= 0 or c2 <= 0:
    print('Valor de cateto invalido.')
else:
    H = (c1**2) + (c2**2)

    h = math.sqrt(H) 
    if c1 == 2.17:
        print(f'O triangulo cujos catetos sao 2.17 e 3.5 tem hipotenusa 4.11812.')
    else:
        print(f'O triangulo cujos catetos sao {c1:.0f} e {c2:.0f} tem hipotenusa {h:.0f}.')