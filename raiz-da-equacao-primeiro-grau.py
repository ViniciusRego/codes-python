coeficientes = input().split()
a = int(coeficientes[0])
b = int(coeficientes[1])

def equacao_primeiro_grau(a,b):
    b = b*-1
    x = b/a
    return x
print(f'{equacao_primeiro_grau(a,b):.2f}')